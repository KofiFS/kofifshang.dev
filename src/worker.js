// kofifshang.dev Worker
//
// Static pages are served from ./public by Cloudflare's asset handler.
// This Worker only handles POST /api/contact: it validates a Start a project
// brief and emails it to Kofi through Cloudflare Email Routing.

import { EmailMessage } from "cloudflare:email";

const FIELDS = {
  name:     { label: "Name",              max: 120,  multiline: false },
  email:    { label: "Email",             max: 254,  multiline: false },
  company:  { label: "Company / project", max: 160,  multiline: false },
  kind:     { label: "Kind of work",      max: 80,   multiline: false },
  timeline: { label: "Timeline",          max: 160,  multiline: false },
  budget:   { label: "Budget range",      max: 120,  multiline: false },
  detail:   { label: "The problem",       max: 8000, multiline: true  },
};

const KINDS = new Set([
  "Backend / platform engineering",
  "Full stack product work",
  "Game development or release",
  "AI product, end to end",
  "Full-time role",
  "Something else",
]);

const MAX_BODY_BYTES = 32 * 1024;
const MIN_FILL_MS = 2500;
// Deliberately excludes whitespace, quotes, angle brackets and separators, so a
// valid address can never break out of the Reply-To header.
const EMAIL_RE = /^[^\s@<>(),;:"\[\]\\]+@[^\s@<>(),;:"\[\]\\]+\.[^\s@<>(),;:"\[\]\\]{2,}$/;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/contact") {
      if (request.method !== "POST") {
        return json({ ok: false, error: "Use POST." }, 405, { Allow: "POST" });
      }
      return handleContact(request, env, url);
    }
    return env.ASSETS.fetch(request);
  },
};

async function handleContact(request, env, url) {
  const origin = request.headers.get("Origin");
  if (origin && origin !== url.origin) {
    return json({ ok: false, error: "Cross-site requests are not accepted." }, 403);
  }

  const type = (request.headers.get("Content-Type") || "").toLowerCase();
  if (!type.startsWith("application/json")) {
    return json({ ok: false, error: "Send the form as JSON." }, 415);
  }

  const text = await request.text();
  if (new TextEncoder().encode(text).length > MAX_BODY_BYTES) {
    return json({ ok: false, error: "That message is too long." }, 413);
  }

  let data;
  try {
    data = JSON.parse(text);
  } catch {
    return json({ ok: false, error: "The form data was malformed." }, 400);
  }
  if (!data || typeof data !== "object" || Array.isArray(data)) {
    return json({ ok: false, error: "The form data was malformed." }, 400);
  }

  // Bot filter: a hidden field humans never see, and a minimum fill time.
  // Report success either way so automated senders learn nothing.
  const elapsed = Number(data.elapsed);
  if (clean(data.website, false) || !Number.isFinite(elapsed) || elapsed < MIN_FILL_MS) {
    return json({ ok: true });
  }

  const f = {};
  for (const [key, spec] of Object.entries(FIELDS)) {
    const value = clean(data[key], spec.multiline);
    if (value.length > spec.max) {
      return json({ ok: false, error: `${spec.label} is too long.` }, 400);
    }
    f[key] = value;
  }

  if (!f.name || !f.email || !f.detail) {
    return json({ ok: false, error: "Name, email and a description of the problem are required." }, 400);
  }
  if (!EMAIL_RE.test(f.email)) {
    return json({ ok: false, error: "That email address doesn't look right." }, 400);
  }
  if (f.kind && !KINDS.has(f.kind)) f.kind = "";

  const from = env.FROM_ADDRESS;
  const to = env.TO_ADDRESS;
  try {
    await env.CONTACT_EMAIL.send(new EmailMessage(from, to, buildMessage(f, from, to)));
  } catch (err) {
    console.error("contact: send failed:", err && err.message ? err.message : err);
    return json({ ok: false, error: "The message couldn't be sent just now." }, 502);
  }

  return json({ ok: true });
}

// Trim, normalise line endings, and strip control characters.
// Single-line fields lose every line break, so nothing can reach a header.
function clean(value, multiline) {
  if (typeof value !== "string") return "";
  let v = value.replace(/\r\n?/g, "\n");
  v = multiline
    ? v.replace(/[\u0000-\u0008\u000B-\u001F\u007F]/g, "")
    : v.replace(/[\u0000-\u001F\u007F]+/g, " ");
  return v.trim();
}

function buildMessage(f, from, to) {
  const who = f.company || f.name;
  const subject = `Project enquiry — ${who}${f.kind ? " · " + f.kind : ""}`;

  const lines = [
    "New project enquiry from kofifshang.dev/start",
    "",
    `Name: ${f.name}`,
    `Email: ${f.email}`,
  ];
  if (f.company) lines.push(`Company / project: ${f.company}`);
  if (f.kind) lines.push(`Kind of work: ${f.kind}`);
  if (f.timeline) lines.push(`Timeline: ${f.timeline}`);
  if (f.budget) lines.push(`Budget range: ${f.budget}`);
  lines.push("", "The problem", "-----------", f.detail, "", "--", `Hit reply to answer ${f.name} directly.`);
  const body = lines.join("\n").replace(/\n/g, "\r\n");

  const domain = from.split("@")[1];
  const headers = [
    `From: "kofifshang.dev contact form" <${from}>`,
    `To: <${to}>`,
    `Reply-To: <${f.email}>`,
    `Subject: ${encodeHeader(subject)}`,
    `Date: ${new Date().toUTCString().replace("GMT", "+0000")}`,
    `Message-ID: <${crypto.randomUUID()}@${domain}>`,
    "MIME-Version: 1.0",
    'Content-Type: text/plain; charset="UTF-8"',
    "Content-Transfer-Encoding: base64",
  ];

  return headers.join("\r\n") + "\r\n\r\n" + wrap(base64(new TextEncoder().encode(body)), 76) + "\r\n";
}

// RFC 2047 encoded-words, split on character boundaries and folded, so long or
// non-ASCII subjects stay within the 75-character word limit.
function encodeHeader(text) {
  if (/^[\x20-\x7E]*$/.test(text) && !text.includes("=?") && text.length <= 900) return text;
  const encoder = new TextEncoder();
  const words = [];
  let chunk = [];
  for (const ch of text) {
    const bytes = encoder.encode(ch);
    if (chunk.length + bytes.length > 45) {
      words.push(chunk);
      chunk = [];
    }
    chunk.push(...bytes);
  }
  if (chunk.length) words.push(chunk);
  return words.map((b) => `=?UTF-8?B?${base64(Uint8Array.from(b))}?=`).join("\r\n ");
}

function base64(bytes) {
  let binary = "";
  for (let i = 0; i < bytes.length; i += 0x8000) {
    binary += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  }
  return btoa(binary);
}

function wrap(text, width) {
  return text.match(new RegExp(`.{1,${width}}`, "g"))?.join("\r\n") ?? "";
}

function json(body, status = 200, extra = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
      ...extra,
    },
  });
}

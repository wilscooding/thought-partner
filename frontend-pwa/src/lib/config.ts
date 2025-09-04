import { dev } from '$app/environment';

/**
 * Read either var name (supports Vercel/Render setups) and normalize to .../api
 * so pages can just call api('/options'), api('/tp-profiles'), etc.
 */
const raw =
  import.meta.env.VITE_API_BASE ??          // prefer already-includes /api
  import.meta.env.VITE_API_URL ??           // host only is fine (we'll add /api)
  '';

const fallback = dev
  ? 'http://localhost:8000'                 // dev host (no /api here; normalization adds it)
  : 'https://tp-backend-ds4h.onrender.com'; // prod host (no /api here; normalization adds it)

function normalizeBase(input: string) {
  const base = (input || fallback).replace(/\/$/, '');
  // Ensure it ends with /api exactly once
  return base.endsWith('/api') ? base : `${base}/api`;
}

export const API_BASE = normalizeBase(raw);

/** Join helper that avoids double slashes. Usage: api('/options') */
export const api = (path: string) =>
  `${API_BASE}${path.startsWith('/') ? path : `/${path}`}`;

// Debug once to verify in console (remove after verifying)
if (dev) console.log('API_BASE =', API_BASE);

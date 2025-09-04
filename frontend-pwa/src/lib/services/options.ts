import { api } from '$lib/config';

let cache: any | null = null;

export async function fetchOptions() {
  if (cache) return cache;
  const res = await fetch(api('/options'));
  if (!res.ok) throw new Error(`GET /options → ${res.status}`);
  cache = await res.json();
  return cache;
}

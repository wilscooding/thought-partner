import httpx, random, asyncio
from typing import Callable

DEFAULT_TIMEOUT = httpx.Timeout(10.0, connect=5.0)
RETRYABLE_STATUS = {408,429, 500, 502, 503, 504}

class RetryingClient(httpx.AsyncClient):
    async def _with_retries(self, fn:Callable, *a, **kw):
        attempt = 0
        while True:
            try:
                response = await fn(*a, **kw)
                if response.status_code in RETRYABLE_STATUS:
                    raise httpx.HTTPStatusError("retryable", request=response.request, response=response)
                return response
            except (httpx.TransportError, httpx.HTTPStatusError) as e:
                attempt += 1
                if attempt >= 4:
                    raise

                sleep = (2 ** (attempt - 1)) + random.random()
                await asyncio.sleep(sleep)

    async def get_retry(self, *a, **kw):  return await self._with_retries(super().get, *a, **kw)
    async def post_retry(self, *a, **kw): return await self._with_retries(super().post, *a, **kw)

client = RetryingClient(timeout=DEFAULT_TIMEOUT, follow_redirects=True)    
    
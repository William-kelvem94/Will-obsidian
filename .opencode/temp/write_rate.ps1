$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'

---

## 7. Rate Limiting e Throttling

Protege a API contra abusos e garante uso justo.

```python
import time
from collections import defaultdict
from flask import request, abort

class RateLimiter:
    def __init__(self, max_requests: int = 100, window: int = 60):
        self._max_requests = max_requests
        self._window = window
        self._requests: dict[str, list[float]] = defaultdict(list)

    def check(self, key: str) -> bool:
        now = time.time()
        window_start = now - self._window
        self._requests[key] = [t for t in self._requests[key] if t > window_start]

        if len(self._requests[key]) >= self._max_requests:
            return False

        self._requests[key].append(now)
        return True

rate_limiter = RateLimiter(max_requests=10, window=60)

@app.before_request
def rate_limit():
    cliente = request.headers.get("X-API-Key") or request.remote_addr
    if not rate_limiter.check(cliente):
        abort(429, "Too Many Requests")
```

```typescript
class RateLimiter {
  private requests = new Map<string, number[]>();

  constructor(
    private maxRequests: number,
    private windowMs: number,
  ) {}

  check(key: string): boolean {
    const now = Date.now();
    const windowStart = now - this.windowMs;
    const timestamps = (this.requests.get(key) ?? []).filter(t => t > windowStart);

    if (timestamps.length >= this.maxRequests) return false;

    timestamps.push(now);
    this.requests.set(key, timestamps);
    return true;
  }
}

const rateLimiter = new RateLimiter(10, 60000);

function rateLimitMiddleware(
  req: express.Request,
  res: express.Response,
  next: express.NextFunction
): void {
  const client = (req.headers["x-api-key"] as string) || req.ip!;
  if (!rateLimiter.check(client)) {
    res.status(429).json({ erro: "Too Many Requests" });
    return;
  }
  next();
}

function rateLimitHeaders(
  req: express.Request,
  res: express.Response,
  next: express.NextFunction
): void {
  res.setHeader("X-RateLimit-Limit", "10");
  res.setHeader("X-RateLimit-Remaining", "7");
  res.setHeader("X-RateLimit-Reset", "60");
  next();
}
```
'@
Add-Content -Path $path -Value $content
Write-Host "OK"

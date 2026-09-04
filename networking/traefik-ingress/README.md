# traefik-ingress

Traefik IngressRoute and middlewares (basic-auth, cors, no-buffering, https-redirect).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `basic-auth-middleware.yaml` | Middleware | Traefik middleware |
| `corsheader-middleware.yaml` | Middleware | Traefik middleware |
| `https-redirect-scheme-middleware.yaml` | Middleware | Traefik middleware |
| `no-buffering-middleware.yaml` | Middleware | Traefik middleware |
| `path-based-routing-ingressroute.yaml` | IngressRoute | Traefik routing |

## Apply

```bash
kubectl apply -f networking/traefik-ingress/
```

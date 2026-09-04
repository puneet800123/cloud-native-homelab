# networking

Ingress, reverse proxying and dynamic DNS.

| Service | Description | Secrets to set |
|---------|-------------|----------------|
| [traefik-ingress](traefik-ingress) | Traefik `IngressRoute` + middlewares (basic-auth, cors, redirects) | none (uses basic-auth Secret) |
| [ingress-nginx](ingress-nginx) | Upstream ingress-nginx controller install (v1.10.1) | none |
| [nginx](nginx) | Standalone nginx (uses shared PVC) | none |
| [cloudflare-ddns](cloudflare-ddns) | Cloudflare DDNS for two zones (one Deployment, two containers) | Cloudflare API key |
| [ddns](ddns) | Cloudflare DDNS for a single zone | Cloudflare API key |
| [ddclient](ddclient) | ddclient-based DDNS (config via hostPath) | none in-manifest |
| [basic-auth](basic-auth) | Shared Traefik basic-auth `Secret` | htpasswd auth string |

Notes:
- `traefik-ingress` references the `traefik-auth-secret` defined in `basic-auth/` via the
  `basic-auth` middleware. Apply `basic-auth/` before the IngressRoute.
- `ingress-nginx/ingress-nginx-install.yaml` is the unmodified upstream manifest for the
  NGINX Ingress Controller — kept as a single file on purpose. `traefik-ingress` and
  `ingress-nginx` are two different ingress approaches; use whichever matches your cluster.
- Replace `example.com` / `example.net` host matches with your own domains.

Apply a single service with `kubectl apply -f networking/<service>/`.

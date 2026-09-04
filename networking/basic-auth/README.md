# basic-auth

Shared Traefik basic-auth Secret used by the traefik-ingress basic-auth middleware.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `traefik-auth-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |

## Values to set (`CHANGE_ME`)

- `auth` in `traefik-auth-secret.yaml`

## Apply

```bash
kubectl apply -f networking/basic-auth/
```

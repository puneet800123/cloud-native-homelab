# vaultwarden

Vaultwarden — Bitwarden-compatible password manager.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `vault-deployment.yaml` | Deployment | workload |
| `vault-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f apps/vaultwarden/
```

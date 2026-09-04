# stremio

Stremio — media streaming front-end.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `stremio-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `stremio-deployment.yaml` | Deployment | workload |
| `stremio-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f apps/stremio/
```

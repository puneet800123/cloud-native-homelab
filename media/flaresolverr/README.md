# flaresolverr

FlareSolverr — solves Cloudflare challenges for indexers.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `flaresolverr-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `flaresolverr-deployment.yaml` | Deployment | workload |
| `flaresolverr-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f media/flaresolverr/
```

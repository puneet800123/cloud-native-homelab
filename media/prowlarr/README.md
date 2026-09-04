# prowlarr

Prowlarr — indexer manager.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `prowlarr-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `prowlarr-deployment.yaml` | Deployment | workload |
| `prowlarr-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f media/prowlarr/
```

# jellyseerr

Jellyseerr — media request manager.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `jellyseerr-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `jellyseerr-deployment.yaml` | Deployment | workload |
| `jellyseerr-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f media/jellyseerr/
```

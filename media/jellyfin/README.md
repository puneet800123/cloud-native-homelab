# jellyfin

Jellyfin — media server.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `jellyfin-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `jellyfin-deployment.yaml` | Deployment | workload |
| `jellyfin-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f media/jellyfin/
```

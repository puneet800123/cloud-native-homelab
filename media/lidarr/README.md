# lidarr

Lidarr — music library automation.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `lidarr-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `lidarr-deployment.yaml` | Deployment | workload |
| `lidarr-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f media/lidarr/
```

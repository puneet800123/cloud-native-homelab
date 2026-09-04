# sonarr

Sonarr — TV library automation.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `sonarr-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `sonarr-deployment.yaml` | Deployment | workload |
| `sonarr-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f media/sonarr/
```

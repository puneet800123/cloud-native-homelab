# bazarr

Bazarr — subtitle automation.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `bazarr-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `bazarr-deployment.yaml` | Deployment | workload |
| `bazarr-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f media/bazarr/
```

# radarr

Radarr — movie library automation.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `radarr-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `radarr-deployment.yaml` | Deployment | workload |
| `radarr-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f media/radarr/
```

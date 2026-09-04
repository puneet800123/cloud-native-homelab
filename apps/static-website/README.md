# static-website

Static website served by nginx from a hostPath web root.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `nginx-config-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `static-site-deployment.yaml` | Deployment | workload |
| `static-site-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f apps/static-website/
```

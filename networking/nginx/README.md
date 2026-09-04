# nginx

Standalone nginx using the shared PVC and a custom nginx.conf.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `nginx-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `nginx-deployment.yaml` | Deployment | workload |
| `nginx-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f networking/nginx/
```

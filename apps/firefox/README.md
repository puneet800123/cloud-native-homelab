# firefox

Containerized Firefox desktop (linuxserver).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `firefox-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `firefox-deployment.yaml` | Deployment | workload |
| `firefox-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f apps/firefox/
```

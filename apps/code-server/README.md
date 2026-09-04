# code-server

code-server (codercom image) — VS Code in the browser.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `code-server-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `code-server-deployment.yaml` | Deployment | workload |
| `code-server-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f apps/code-server/
```

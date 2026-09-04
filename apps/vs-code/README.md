# vs-code

code-server (linuxserver image) — VS Code in the browser.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `vs-code-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `vs-code-deployment.yaml` | Deployment | workload |
| `vs-code-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `vs-code-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `PASSWORD` in `vs-code-secret.yaml`

## Apply

```bash
kubectl apply -f apps/vs-code/
```

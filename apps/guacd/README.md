# guacd

guacd — the Guacamole proxy daemon (backend for guacamole).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `guacd-deployment.yaml` | Deployment | workload |
| `guacd-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f apps/guacd/
```

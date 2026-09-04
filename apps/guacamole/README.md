# guacamole

Apache Guacamole — clientless remote desktop gateway. Backed by guacd and the shared Postgres.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `guacamole-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `guacamole-deployment.yaml` | Deployment | workload |
| `guacamole-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `guacamole-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `POSTGRES_PASSWORD` in `guacamole-secret.yaml`

## Apply

```bash
kubectl apply -f apps/guacamole/
```

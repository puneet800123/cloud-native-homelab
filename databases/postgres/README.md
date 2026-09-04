# postgres

PostgreSQL — a shared instance and a pgvecto-rs instance for Immich.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `immich-postgres-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `immich-postgres-deployment.yaml` | Deployment | workload |
| `immich-postgres-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `immich-postgres-service.yaml` | Service | network service |
| `postgres-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `postgres-deployment.yaml` | Deployment | workload |
| `postgres-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `postgres-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `POSTGRES_PASSWORD` in `immich-postgres-secret.yaml`
- `POSTGRES_PASSWORD` in `postgres-secret.yaml`

## Apply

```bash
kubectl apply -f databases/postgres/
```

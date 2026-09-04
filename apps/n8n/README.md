# n8n

n8n — workflow automation. Uses the shared Postgres and basic auth.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `n8n-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `n8n-deployment.yaml` | Deployment | workload |
| `n8n-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `n8n-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `DB_POSTGRESDB_PASSWORD` in `n8n-secret.yaml`
- `N8N_BASIC_AUTH_USER` in `n8n-secret.yaml`
- `N8N_BASIC_AUTH_PASSWORD` in `n8n-secret.yaml`

## Apply

```bash
kubectl apply -f apps/n8n/
```

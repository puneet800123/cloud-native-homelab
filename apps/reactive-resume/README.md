# reactive-resume

Reactive Resume — resume builder. Uses Postgres and MinIO.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `reactive-resume-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `reactive-resume-deployment.yaml` | Deployment | workload |
| `reactive-resume-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `reactive-resume-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `DATABASE_URL` in `reactive-resume-secret.yaml`
- `JWT_SECRET` in `reactive-resume-secret.yaml`
- `ACCESS_TOKEN_SECRET` in `reactive-resume-secret.yaml`
- `REFRESH_TOKEN_SECRET` in `reactive-resume-secret.yaml`
- `CHROME_TOKEN` in `reactive-resume-secret.yaml`
- `STORAGE_ACCESS_KEY` in `reactive-resume-secret.yaml`
- `STORAGE_SECRET_KEY` in `reactive-resume-secret.yaml`

## Apply

```bash
kubectl apply -f apps/reactive-resume/
```

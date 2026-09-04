# minio

MinIO — S3-compatible object storage.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `minio-deployment.yaml` | Deployment | workload |
| `minio-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `minio-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `MINIO_ROOT_USER` in `minio-secret.yaml`
- `MINIO_ROOT_PASSWORD` in `minio-secret.yaml`

## Apply

```bash
kubectl apply -f databases/minio/
```

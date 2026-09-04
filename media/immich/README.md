# immich

Immich — self-hosted photo/video backup (server, machine-learning, redis).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `immich-machine-learning-deployment.yaml` | Deployment | workload |
| `immich-machine-learning-service.yaml` | Service | network service |
| `immich-redis-deployment.yaml` | Deployment | workload |
| `immich-redis-service.yaml` | Service | network service |
| `immich-server-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `immich-server-deployment.yaml` | Deployment | workload |
| `immich-server-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `immich-server-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `DB_PASSWORD` in `immich-server-secret.yaml`

## Apply

```bash
kubectl apply -f media/immich/
```

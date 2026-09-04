# frigate

Frigate — NVR with object detection (privileged, hardware accel).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `frigate-deployment.yaml` | Deployment | workload |
| `frigate-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `frigate-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `FRIGATE_RTSP_PASSWORD` in `frigate-secret.yaml`

## Apply

```bash
kubectl apply -f smart-home/frigate/
```

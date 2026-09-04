# ddns

Cloudflare dynamic DNS for a single zone. Uses the shared PVC.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `ddns-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `ddns-deployment.yaml` | Deployment | workload |
| `ddns-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `ddns-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `API_KEY` in `ddns-secret.yaml`

## Apply

```bash
kubectl apply -f networking/ddns/
```

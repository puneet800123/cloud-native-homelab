# cloudflare-ddns

Cloudflare dynamic DNS for two zones (one Deployment, two containers).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `cloudflare-ddns-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `cloudflare-ddns-deployment.yaml` | Deployment | workload |
| `cloudflare-ddns-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |

## Values to set (`CHANGE_ME`)

- `API_KEY` in `cloudflare-ddns-secret.yaml`

## Apply

```bash
kubectl apply -f networking/cloudflare-ddns/
```

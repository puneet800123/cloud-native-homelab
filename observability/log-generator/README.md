# log-generator

Demo workload: a busybox log generator plus a Fleet-enrolled Elastic Agent.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `elastic-agent-certs-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `log-generator-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `log-generator-deployment.yaml` | Deployment | workload |
| `log-generator-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |

## Values to set (`CHANGE_ME`)

- `ca.crt` in `elastic-agent-certs-secret.yaml`
- `FLEET_ENROLLMENT_TOKEN` in `log-generator-secret.yaml`

## Apply

```bash
kubectl apply -f observability/log-generator/
```

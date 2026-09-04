# logstash

Logstash — Beats-to-Elasticsearch pipeline with mTLS.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `logstash-certs-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `logstash-config-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `logstash-deployment.yaml` | Deployment | workload |
| `logstash-env-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `logstash-pipeline-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `logstash-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `ca.crt` in `logstash-certs-secret.yaml`
- `tls.crt` in `logstash-certs-secret.yaml`
- `tls.key` in `logstash-certs-secret.yaml`

## Apply

```bash
kubectl apply -f observability/logstash/
```

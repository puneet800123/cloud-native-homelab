# elasticsearch

Elasticsearch StatefulSet with security and TLS enabled.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `elastic-certs-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `elasticsearch-config-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `elasticsearch-credentials-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `elasticsearch-env-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `elasticsearch-service.yaml` | Service | network service |
| `elasticsearch-statefulset.yaml` | StatefulSet | workload (stateful) |

## Values to set (`CHANGE_ME`)

- `ca.crt` in `elastic-certs-secret.yaml`
- `tls.crt` in `elastic-certs-secret.yaml`
- `tls.key` in `elastic-certs-secret.yaml`
- `password` in `elasticsearch-credentials-secret.yaml`

## Apply

```bash
kubectl apply -f observability/elasticsearch/
```

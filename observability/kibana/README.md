# kibana

Kibana — the Elastic stack UI.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `kibana-certs-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `kibana-config-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `kibana-deployment.yaml` | Deployment | workload |
| `kibana-encryption-keys-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `kibana-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `ca.crt` in `kibana-certs-secret.yaml`
- `tls.crt` in `kibana-certs-secret.yaml`
- `tls.key` in `kibana-certs-secret.yaml`
- `XPACK_ENCRYPTEDSAVEDOBJECTS_ENCRYPTIONKEY` in `kibana-encryption-keys-secret.yaml`
- `XPACK_SECURITY_ENCRYPTIONKEY` in `kibana-encryption-keys-secret.yaml`
- `XPACK_REPORTING_ENCRYPTIONKEY` in `kibana-encryption-keys-secret.yaml`

## Apply

```bash
kubectl apply -f observability/kibana/
```

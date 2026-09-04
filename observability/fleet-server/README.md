# fleet-server

Elastic Agent Fleet Server.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `fleet-server-certs-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `fleet-server-clusterrole.yaml` | ClusterRole | RBAC role |
| `fleet-server-clusterrolebinding.yaml` | ClusterRoleBinding | RBAC binding |
| `fleet-server-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `fleet-server-deployment.yaml` | Deployment | workload |
| `fleet-server-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `fleet-server-service.yaml` | Service | network service |
| `fleet-server-serviceaccount.yaml` | ServiceAccount | service account |

## Values to set (`CHANGE_ME`)

- `ca.crt` in `fleet-server-certs-secret.yaml`
- `tls.crt` in `fleet-server-certs-secret.yaml`
- `tls.key` in `fleet-server-certs-secret.yaml`
- `FLEET_SERVER_SERVICE_TOKEN` in `fleet-server-secret.yaml`

## Apply

```bash
kubectl apply -f observability/fleet-server/
```

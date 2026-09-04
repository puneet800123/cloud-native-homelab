# grafana

Grafana — dashboards and visualization. Comes pre-provisioned with Prometheus as
the default datasource.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `grafana-secret.yaml` | Secret | admin credentials (fill in CHANGE_ME) |
| `grafana-datasources-configmap.yaml` | ConfigMap | provisioned Prometheus datasource |
| `grafana-deployment.yaml` | Deployment | workload |
| `grafana-service.yaml` | Service | network service (NodePort, :80 → 3000) |

## Values to set (`CHANGE_ME`)

- `GF_SECURITY_ADMIN_USER` in `grafana-secret.yaml`
- `GF_SECURITY_ADMIN_PASSWORD` in `grafana-secret.yaml`

## Notes

- The datasource points at `http://prometheus:9090` (the Prometheus Service).
- Storage uses a `hostPath` at `/mnt/apps/grafana`; swap for a PVC in a
  multi-node cluster.

## Apply

```bash
kubectl apply -f observability/grafana/
```

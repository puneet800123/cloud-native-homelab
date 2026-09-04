# prometheus

Prometheus — metrics collection and time-series database. Scrapes node-exporter,
kube-state-metrics, the Kubernetes API server, and any pod annotated with
`prometheus.io/scrape: "true"`.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `prometheus-serviceaccount.yaml` | ServiceAccount | service account |
| `prometheus-clusterrole.yaml` | ClusterRole | RBAC role (service discovery) |
| `prometheus-clusterrolebinding.yaml` | ClusterRoleBinding | RBAC binding |
| `prometheus-configmap.yaml` | ConfigMap | scrape configuration (`prometheus.yml`) |
| `prometheus-deployment.yaml` | Deployment | workload |
| `prometheus-service.yaml` | Service | network service (ClusterIP, port 9090) |

## Notes

- Storage uses a `hostPath` at `/mnt/apps/prometheus`; swap for a PVC in a
  multi-node cluster.
- Grafana reads from this service at `http://prometheus:9090`.

## Apply

```bash
kubectl apply -f observability/prometheus/
```

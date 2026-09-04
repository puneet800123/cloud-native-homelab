# kube-state-metrics

kube-state-metrics — exposes metrics about the state of Kubernetes objects
(deployments, pods, nodes, jobs, etc.) for Prometheus to scrape.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `kube-state-metrics-serviceaccount.yaml` | ServiceAccount | service account |
| `kube-state-metrics-clusterrole.yaml` | ClusterRole | read-only RBAC over cluster objects |
| `kube-state-metrics-clusterrolebinding.yaml` | ClusterRoleBinding | RBAC binding |
| `kube-state-metrics-deployment.yaml` | Deployment | workload |
| `kube-state-metrics-service.yaml` | Service | headless service (metrics 8080, telemetry 8081) |

## Notes

- The Service is headless (`clusterIP: None`); Prometheus scrapes it via the
  `kube-state-metrics` job.

## Apply

```bash
kubectl apply -f observability/kube-state-metrics/
```

# radar

Radar — cluster resource visualizer (read-only RBAC).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `radar-clusterrole.yaml` | ClusterRole | RBAC role |
| `radar-clusterrolebinding.yaml` | ClusterRoleBinding | RBAC binding |
| `radar-deployment.yaml` | Deployment | workload |
| `radar-service.yaml` | Service | network service |
| `radar-serviceaccount.yaml` | ServiceAccount | service account |

## Apply

```bash
kubectl apply -f observability/radar/
```

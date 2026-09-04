# homepage

Homepage — dashboard/start page. Uses a ServiceAccount with read-only cluster RBAC to show cluster info.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `homepage-clusterrole.yaml` | ClusterRole | RBAC role |
| `homepage-clusterrolebinding.yaml` | ClusterRoleBinding | RBAC binding |
| `homepage-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `homepage-deployment.yaml` | Deployment | workload |
| `homepage-service.yaml` | Service | network service |
| `homepage-serviceaccount-token-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `homepage-serviceaccount.yaml` | ServiceAccount | service account |

## Apply

```bash
kubectl apply -f apps/homepage/
```

# portainer

Portainer — container management UI (bound to cluster-admin).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `portainer-clusterrolebinding.yaml` | ClusterRoleBinding | RBAC binding |
| `portainer-deployment.yaml` | Deployment | workload |
| `portainer-service.yaml` | Service | network service |
| `portainer-serviceaccount.yaml` | ServiceAccount | service account |

## Apply

```bash
kubectl apply -f apps/portainer/
```

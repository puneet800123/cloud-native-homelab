# fluent-bit

Fluent Bit log forwarder (DaemonSet) shipping to VictoriaLogs.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `fluent-bit-clusterrole.yaml` | ClusterRole | RBAC role |
| `fluent-bit-clusterrolebinding.yaml` | ClusterRoleBinding | RBAC binding |
| `fluent-bit-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `fluent-bit-daemonset.yaml` | DaemonSet | per-node workload |
| `fluent-bit-serviceaccount.yaml` | ServiceAccount | service account |

## Apply

```bash
kubectl apply -f observability/fluent-bit/
```

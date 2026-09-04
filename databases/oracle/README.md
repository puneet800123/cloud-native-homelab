# oracle

Oracle XE database plus an ORDS/APEX node.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `oracle-db-deployment.yaml` | Deployment | workload |
| `oracle-db-service.yaml` | Service | network service |
| `oracle-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `ords-node-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `ords-node-deployment.yaml` | Deployment | workload |
| `ords-node-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `ORACLE_PWD` in `oracle-secret.yaml`

## Apply

```bash
kubectl apply -f databases/oracle/
```

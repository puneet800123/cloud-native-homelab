# wordpress

WordPress with MariaDB and phpMyAdmin.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `mariadb-deployment.yaml` | Deployment | workload |
| `mariadb-secret.yaml` | Secret | secret material (fill in CHANGE_ME) |
| `mariadb-service.yaml` | Service | network service |
| `phpmyadmin-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `phpmyadmin-deployment.yaml` | Deployment | workload |
| `phpmyadmin-service.yaml` | Service | network service |
| `wordpress-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `wordpress-deployment.yaml` | Deployment | workload |
| `wordpress-service.yaml` | Service | network service |

## Values to set (`CHANGE_ME`)

- `mysql-root-password` in `mariadb-secret.yaml`
- `mysql-user` in `mariadb-secret.yaml`
- `mysql-password` in `mariadb-secret.yaml`
- `mysql-database` in `mariadb-secret.yaml`

## Apply

```bash
kubectl apply -f databases/wordpress/
```

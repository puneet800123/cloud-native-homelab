# databases

Databases and database tooling. Apply these before the applications that depend on them.

| Service | Description | Secrets to set |
|---------|-------------|----------------|
| [postgres](postgres) | Two PostgreSQL instances: a shared `postgres` and a pgvecto-rs `immich-postgres` | superuser passwords |
| [oracle](oracle) | Oracle XE database + ORDS/APEX node | Oracle password |
| [minio](minio) | S3-compatible object storage | root user + password |
| [wordpress](wordpress) | WordPress + MariaDB + phpMyAdmin | MariaDB credentials |

Notes:
- The shared `postgres` instance is used by `n8n`, `guacamole` and `reactive-resume`.
  Keep the `POSTGRES_PASSWORD` in `postgres/postgres-secret.yaml` in sync with those services.
- The `immich-postgres` instance backs `media/immich`.

Apply a single service with `kubectl apply -f databases/<service>/`.

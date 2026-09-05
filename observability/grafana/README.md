# grafana

Grafana — dashboards and visualization. Comes pre-provisioned with Prometheus as
the default datasource, and is configured so its panels can be embedded in an
`<iframe>` on an external site (e.g. the portfolio dashboard).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `grafana-secret.yaml` | Secret | admin credentials (fill in CHANGE_ME) |
| `grafana-datasources-configmap.yaml` | ConfigMap | provisioned Prometheus datasource |
| `grafana-embedding-configmap.yaml` | ConfigMap | iframe embedding + anonymous viewing settings |
| `grafana-deployment.yaml` | Deployment | workload (runs as uid 472, init container fixes data-dir perms) |
| `grafana-service.yaml` | Service | network service (NodePort, :80 → 3000) |

## Values to set (`CHANGE_ME`)

- `GF_SECURITY_ADMIN_USER` in `grafana-secret.yaml`
- `GF_SECURITY_ADMIN_PASSWORD` in `grafana-secret.yaml`
- `GF_SERVER_ROOT_URL` in `grafana-embedding-configmap.yaml` (public URL Grafana is served on)

## iframe embedding

`grafana-embedding-configmap.yaml` sets:

- `GF_SECURITY_ALLOW_EMBEDDING=true` — removes the `X-Frame-Options: deny` header so
  panels can load inside an `<iframe>`.
- `GF_AUTH_ANONYMOUS_ENABLED=true` + `GF_AUTH_ANONYMOUS_ORG_ROLE=Viewer` — lets visitors
  view embedded panels without logging in.
- `GF_SECURITY_COOKIE_SAMESITE=none` — required for cross-origin iframe cookies.

Embed a single panel with the panel's share → embed URL, e.g.:

```html
<iframe src="http://<grafana-host>/d-solo/<dashboard-uid>/<slug>?panelId=1&theme=dark"
        width="450" height="200" frameborder="0"></iframe>
```

## Notes

- The datasource points at `http://prometheus:9090` (the Prometheus Service).
- Storage uses a `hostPath` at `/mnt/apps/grafana`; swap for a PVC in a
  multi-node cluster.
- The admin `Secret` holds `CHANGE_ME` in git — create the real Secret out-of-band
  (or via your secret manager) before applying.

## Apply

```bash
kubectl apply -f observability/grafana/
```

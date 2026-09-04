# node-exporter

Prometheus node-exporter — exposes per-node host metrics (CPU, memory, disk,
network). Runs as a DaemonSet on every node.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `node-exporter-daemonset.yaml` | DaemonSet | per-node workload |
| `node-exporter-service.yaml` | Service | headless service for scrape discovery |

## Notes

- Uses `hostNetwork` + `hostPID` and mounts `/proc`, `/sys`, `/` read-only to read
  host metrics; binds `hostPort` 9100.
- A toleration lets it run on control-plane nodes too.
- The Service is headless (`clusterIP: None`) so Prometheus discovers each node's
  endpoint individually (job `node-exporter`).

## Apply

```bash
kubectl apply -f observability/node-exporter/
```

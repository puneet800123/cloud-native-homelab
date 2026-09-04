# qbittorrent

qBittorrent — torrent client.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `qbittorrent-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `qbittorrent-deployment.yaml` | Deployment | workload |
| `qbittorrent-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f media/qbittorrent/
```

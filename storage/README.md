# storage

Cluster storage primitives. Apply this first — several workloads depend on the
`pv-claim` PersistentVolumeClaim defined here.

| Resource | File | Description |
|----------|------|-------------|
| StorageClass | [local-storage](local-storage/local-storage-storageclass.yaml) | `local-storage`, no-provisioner, WaitForFirstConsumer |
| PersistentVolume | [pv-volume](local-storage/pv-volume-persistentvolume.yaml) | 500Gi local volume at `/apps`, bound to `pv-claim` |
| PersistentVolumeClaim | [pv-claim](local-storage/pv-claim-persistentvolumeclaim.yaml) | 500Gi RWX claim used by `nginx` and `ddns` |

Consumers of `pv-claim`: `networking/nginx`, `networking/ddns`.

Set the node hostname in `local-storage/pv-volume-persistentvolume.yaml`
(`nodeAffinity` → currently `CHANGE_ME`/`photon-os`) to match your node
(`kubectl get nodes`).

```bash
kubectl apply -f storage/local-storage/
```

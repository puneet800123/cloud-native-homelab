# local-storage

Local StorageClass, PersistentVolume and PersistentVolumeClaim.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `local-storage-storageclass.yaml` | StorageClass | storage class |
| `pv-claim-persistentvolumeclaim.yaml` | PersistentVolumeClaim | persistent volume claim |
| `pv-volume-persistentvolume.yaml` | PersistentVolume | persistent volume |

## Apply

```bash
kubectl apply -f storage/local-storage/
```

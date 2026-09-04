# inverter-ocr

Custom Flask OCR service that reads an inverter's LCD. Source and Dockerfile live in scripts/inverter-ocr.

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `inverter-ocr-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `inverter-ocr-deployment.yaml` | Deployment | workload |
| `inverter-ocr-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f apps/inverter-ocr/
```

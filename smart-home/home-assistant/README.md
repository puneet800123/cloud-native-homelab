# home-assistant

Home Assistant — home automation hub (hostNetwork, privileged).

## Manifests

| File | Kind | Purpose |
|------|------|---------|
| `home-assistant-configmap.yaml` | ConfigMap | non-sensitive configuration |
| `homeassistant-deployment.yaml` | Deployment | workload |
| `homeassistant-service.yaml` | Service | network service |

## Apply

```bash
kubectl apply -f smart-home/home-assistant/
```

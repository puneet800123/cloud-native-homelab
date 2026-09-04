# cloud-native-homelab

Kubernetes manifests for a self-hosted homelab, organized by category and service.
Every deployment is broken into individual manifests (`<service>-<kind>.yaml`), and
all configuration is externalized into **ConfigMaps** (non-sensitive) and **Secrets**
(sensitive). No secret values are committed — every secret field holds the placeholder
`CHANGE_ME` that you must fill in before applying.

## Repository layout

```
.
├── apps/            # General self-hosted applications
├── databases/       # Databases and DB tooling
├── media/           # Media server + *arr automation stack
├── networking/      # Ingress, reverse proxy, DDNS
├── observability/   # Logging / monitoring (Elastic stack, VictoriaLogs, etc.)
├── smart-home/      # Home Assistant, cameras, MQTT
├── storage/         # StorageClass / PersistentVolume / PVC
└── scripts/         # Standalone helper scripts (not Kubernetes manifests)
```

Each category has its own `README.md` describing the services in it, and each service
folder has a `README.md` listing its manifests and the `CHANGE_ME` values to fill in.

## Service index

| Category | Service | Description |
|----------|---------|-------------|
| apps | [cloudbeaver](apps/cloudbeaver) | Web-based database manager |
| apps | [code-server](apps/code-server) | VS Code in the browser (coder) |
| apps | [vs-code](apps/vs-code) | VS Code in the browser (linuxserver) |
| apps | [fileserver](apps/fileserver) | File browser web UI |
| apps | [firefox](apps/firefox) | Containerized Firefox |
| apps | [guacamole](apps/guacamole) | Clientless remote desktop gateway |
| apps | [guacd](apps/guacd) | Guacamole proxy daemon |
| apps | [homepage](apps/homepage) | Dashboard / start page |
| apps | [inverter-ocr](apps/inverter-ocr) | OCR service for inverter LCD (custom) |
| apps | [n8n](apps/n8n) | Workflow automation |
| apps | [portainer](apps/portainer) | Container management UI |
| apps | [reactive-resume](apps/reactive-resume) | Resume builder |
| apps | [static-website](apps/static-website) | Static site served by nginx |
| apps | [stremio](apps/stremio) | Media streaming front-end |
| apps | [vaultwarden](apps/vaultwarden) | Bitwarden-compatible password manager |
| databases | [postgres](databases/postgres) | PostgreSQL (shared + immich instance) |
| databases | [oracle](databases/oracle) | Oracle XE + ORDS/APEX |
| databases | [minio](databases/minio) | S3-compatible object storage |
| databases | [wordpress](databases/wordpress) | WordPress + MariaDB + phpMyAdmin |
| media | [immich](media/immich) | Photo/video backup (server, ML, redis) |
| media | [jellyfin](media/jellyfin) | Media server |
| media | [qbittorrent](media/qbittorrent) | Torrent client |
| media | [radarr](media/radarr) | Movie automation |
| media | [sonarr](media/sonarr) | TV automation |
| media | [lidarr](media/lidarr) | Music automation |
| media | [bazarr](media/bazarr) | Subtitle automation |
| media | [prowlarr](media/prowlarr) | Indexer manager |
| media | [jellyseerr](media/jellyseerr) | Media request manager |
| media | [flaresolverr](media/flaresolverr) | Cloudflare challenge solver |
| observability | [elasticsearch](observability/elasticsearch) | Search/analytics store |
| observability | [kibana](observability/kibana) | Elastic UI |
| observability | [logstash](observability/logstash) | Log pipeline |
| observability | [fluent-bit](observability/fluent-bit) | Log forwarder (DaemonSet) |
| observability | [fleet-server](observability/fleet-server) | Elastic Agent Fleet Server |
| observability | [log-generator](observability/log-generator) | Demo log workload + agent |
| observability | [victorialogs](observability/victorialogs) | Lightweight log database |
| observability | [radar](observability/radar) | Cluster resource visualizer |
| networking | [traefik-ingress](networking/traefik-ingress) | Traefik IngressRoute + middlewares |
| networking | [ingress-nginx](networking/ingress-nginx) | ingress-nginx controller (upstream) |
| networking | [nginx](networking/nginx) | Standalone nginx |
| networking | [cloudflare-ddns](networking/cloudflare-ddns) | Cloudflare DDNS (multi-zone) |
| networking | [ddns](networking/ddns) | Cloudflare DDNS (single zone) |
| networking | [ddclient](networking/ddclient) | ddclient DDNS |
| networking | [basic-auth](networking/basic-auth) | Shared Traefik basic-auth Secret |
| smart-home | [home-assistant](smart-home/home-assistant) | Home automation hub |
| smart-home | [frigate](smart-home/frigate) | NVR with object detection |
| smart-home | [go2rtc](smart-home/go2rtc) | Camera stream aggregator |
| smart-home | [mqtt](smart-home/mqtt) | Mosquitto MQTT broker |
| storage | [local-storage](storage/local-storage) | Local StorageClass/PV/PVC |

## Before you apply anything

1. **Fill in secrets.** Search the repo for the placeholder and replace each with a real value:
   ```bash
   grep -rn "CHANGE_ME" .
   ```
2. **Do not commit real secrets.** The `.gitignore` blocks `*.env` and `secrets.*.yaml`;
   consider managing real secrets out-of-band (SOPS, sealed-secrets, an external secret store).
3. **Apply storage first**, then databases, then the apps that depend on them.

Example (apply an entire service folder):
```bash
kubectl apply -f apps/n8n/
```

Example (apply a whole category):
```bash
kubectl apply -R -f observability/
```

## Notes

- Domains in the manifests use `example.com` / `example.net` placeholders — replace with your own.
- Several workloads use `hostPath` volumes with `/mnt/...` paths tied to a single-node
  setup; adjust these to your environment.
- `scripts/` contains standalone helpers (a Playwright YouTube player and the inverter-OCR
  Flask app + Dockerfile). Their Python virtualenvs are intentionally not committed.

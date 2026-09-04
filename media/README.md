# media

Media server and the "*arr" automation stack.

| Service | Description | Secrets to set |
|---------|-------------|----------------|
| [immich](immich) | Photo/video backup: server + machine-learning + redis | DB password |
| [jellyfin](jellyfin) | Media server | none |
| [qbittorrent](qbittorrent) | Torrent client | none |
| [radarr](radarr) | Movie library automation | none |
| [sonarr](sonarr) | TV library automation | none |
| [lidarr](lidarr) | Music library automation | none |
| [bazarr](bazarr) | Subtitle automation | none |
| [prowlarr](prowlarr) | Indexer manager | none |
| [jellyseerr](jellyseerr) | Media request manager | none |
| [flaresolverr](flaresolverr) | Cloudflare challenge solver (used by prowlarr) | none |

Notes:
- `immich` depends on `databases/postgres` (the `immich-postgres` instance). The
  `DB_PASSWORD` in `immich/immich-server-secret.yaml` must match
  `databases/postgres/immich-postgres-secret.yaml`.
- Most services share `/mnt/media/*` and `/mnt/config/*` hostPath layouts and use
  `PUID`/`PGID`/`TZ` config (see each service's ConfigMap).

Apply a single service with `kubectl apply -f media/<service>/`.

# apps

General-purpose self-hosted applications.

| Service | Description | Secrets to set |
|---------|-------------|----------------|
| [cloudbeaver](cloudbeaver) | Web-based database manager | none |
| [code-server](code-server) | VS Code in the browser (codercom image) | none |
| [vs-code](vs-code) | VS Code in the browser (linuxserver image) | login password |
| [fileserver](fileserver) | Filebrowser web UI | none |
| [firefox](firefox) | Containerized Firefox desktop | none |
| [guacamole](guacamole) | Clientless remote desktop gateway | Postgres password |
| [guacd](guacd) | Guacamole proxy daemon (backend for guacamole) | none |
| [homepage](homepage) | Dashboard / start page (needs RBAC to read cluster) | none |
| [inverter-ocr](inverter-ocr) | Custom Flask OCR service (see `scripts/inverter-ocr`) | none |
| [n8n](n8n) | Workflow automation | DB password + basic-auth creds |
| [portainer](portainer) | Container management UI (cluster-admin) | none |
| [reactive-resume](reactive-resume) | Resume builder | DB URL, JWT/token secrets, MinIO keys |
| [static-website](static-website) | Static site served by nginx | none |
| [stremio](stremio) | Media streaming front-end | none |
| [vaultwarden](vaultwarden) | Bitwarden-compatible password manager | none |

Apply a single service with `kubectl apply -f apps/<service>/`.

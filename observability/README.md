# observability

Logging and monitoring. Two independent stacks live here: the **Elastic stack**
(Elasticsearch → Kibana + Logstash + Fleet/Agents) and a lightweight
**Fluent Bit → VictoriaLogs** pipeline. `radar` is a cluster resource visualizer.

| Service | Description | Secrets to set |
|---------|-------------|----------------|
| [elasticsearch](elasticsearch) | Search/analytics store (StatefulSet, TLS + security on) | `elastic` password, TLS certs |
| [kibana](kibana) | Elastic UI | ES password, encryption keys, TLS certs |
| [logstash](logstash) | Beats → Elasticsearch pipeline (mTLS) | ES password, TLS certs |
| [fleet-server](fleet-server) | Elastic Agent Fleet Server | service token, TLS certs |
| [log-generator](log-generator) | Demo workload: busybox logs + enrolled agent | enrollment token, CA cert |
| [fluent-bit](fluent-bit) | Node-level log forwarder (DaemonSet) → VictoriaLogs | none |
| [victorialogs](victorialogs) | Lightweight log database | none |
| [radar](radar) | Cluster resource visualizer (read-only RBAC) | none |

## Elastic stack: shared secrets & TLS

Several services reference secrets that you must populate:

- **`elasticsearch-credentials`** (in `elasticsearch/`): the `elastic` superuser password,
  consumed by elasticsearch, kibana and logstash.
- **`kibana-encryption-keys`** (in `kibana/`): three 32+ char random keys.
  Generate each with `openssl rand -hex 32`.
- **`fleet-server-secret`** (in `fleet-server/`): the Fleet Server service token,
  created in Kibana → Fleet → Settings.
- **`log-generator-agent-secret`** (in `log-generator/`): an Elastic Agent enrollment token
  from the Kibana Fleet UI.

TLS certificate Secrets are placeholders (`elastic-certs`, `kibana-certs`, `logstash-certs`,
`fleet-server-certs`, `elastic-agent-certs`). Generate a CA and per-service certs, then recreate
each Secret from the real files, for example:

```bash
kubectl create secret generic elastic-certs \
  --from-file=ca.crt --from-file=tls.crt --from-file=tls.key \
  --dry-run=client -o yaml > elasticsearch/elastic-certs-secret.yaml
```

Apply order: `elasticsearch` → `kibana` → `logstash` → `fleet-server` → `log-generator`.

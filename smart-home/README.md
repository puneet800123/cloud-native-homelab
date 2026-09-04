# smart-home

Home automation and camera/streaming services.

| Service | Description | Secrets to set |
|---------|-------------|----------------|
| [home-assistant](home-assistant) | Home automation hub (hostNetwork, privileged) | none |
| [frigate](frigate) | NVR with object detection (privileged, GPU/dev access) | RTSP password |
| [go2rtc](go2rtc) | Camera stream aggregator (hostNetwork) | none |
| [mqtt](mqtt) | Mosquitto MQTT broker | none |

Notes:
- `home-assistant` and `go2rtc` use `hostNetwork: true`; only one pod can bind their host
  ports per node.
- `frigate` runs privileged and mounts `/dev/dri` for hardware acceleration.

Apply a single service with `kubectl apply -f smart-home/<service>/`.

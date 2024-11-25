# /bin/bash

envsubst '${DS_PROMETHEUS}' < base_gpu_exporter.json > gpu_exporters.json

# cat /var/lib/grafana/dashboards/gpu_exporter.json
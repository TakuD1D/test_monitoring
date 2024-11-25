FROM grafana/grafana

# copy
COPY ./grafana/dashboard /var/lib/grafana/dashboards

USER root
# 必要なもの
RUN apk update && \
    apk add jq && \
    apk add curl && \
    apk add envsubst

ENV DS_PROMETHEUS=prometheus-server-uid

WORKDIR /var/lib/grafana/dashboards/
RUN bash /var/lib/grafana/dashboards/json_sub.sh
# shコマンド

# CMD [ "bash","json_sub.sh" ]


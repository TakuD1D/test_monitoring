import json
import prometheus_client
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY, Gauge, CollectorRegistry
from prometheus_client.registry import Collector
import time
import subprocess
import re
import threading


class CustomCollector(Collector):
    def collect(self):
        metrics = [
            "CPUPerc",
            "MemPerc",
            "NetIO"
        ]
        metrics_name = [
            "CPU-Usage",
            "Memory-Usage",
            # "Network-I/O"
        ]
        g = GaugeMetricFamily("docker_container_metrics", 'each docker metrics', labels=['container_name','metric_type'])
        stats = get_docker_stats()
        for metric, metric_name in zip(metrics, metrics_name):
            for stat in stats:
                percent_stat = re.sub('%','',stat[metric])
                g.add_metric([stat['Name'], metric_name], percent_stat)
            
        yield g
        

def get_docker_stats():
    stats = subprocess.run(['docker', 'stats', '--no-stream', '--format=json'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    stats = stats.split('\n')
    list_stats = [  json.loads(stat) for stat in stats if stat != '']
    return list_stats


if __name__ == '__main__':
    collect = CollectorRegistry(auto_describe=False)
    collect.register(CustomCollector())
    start_http_server(9999, registry=collect)
    while True:
        time.sleep(1)
    
    
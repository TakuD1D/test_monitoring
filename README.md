# test_monitoring
## Exporter
- Goでのexporter未実装です。
- Goだとマルチビルドステージでイメージを超小さくできるのでよければ
  - https://pkg.go.dev/github.com/prometheus/client_golang/prometheus
- Pythonでのexporter (docker_exporter)
  - Dockerごとのメトリクスを取得しています
- grafanaにはダッシュボードのjsonファイルとその設定を記述しています。
- Prom_configにはalertmanagerとpromethuesの設定が入っています。
  - alertmanagerはPromQLに条件式を書き条件を満たすとslackにアラートを投げることができるコンポーネント

 ### 参考記事
- https://zenn.dev/aobaiwaki/articles/a612bf497c59ca
- https://zenn.dev/aobaiwaki/articles/5b1655bde00230#alert-manager%E3%82%92%E7%AB%8B%E3%81%A1%E4%B8%8A%E3%81%92%E3%82%8B
- https://zenn.dev/kou_kawa/articles/34-aws-grafana-prometheus
- https://qiita.com/Esfahan/items/0feaedfd771f49ac7ee4

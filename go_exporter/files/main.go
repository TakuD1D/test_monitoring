package main

import (
	"fmt"
	_ "github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"net/http"
)

func main() {
	fmt.Println('a')
	http.Handle("/metrics", promhttp.Handler())
	http.ListenAndServe(":2112", nil)
}
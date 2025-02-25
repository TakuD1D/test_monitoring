FROM golang:latest AS builder

WORKDIR /go/src/app

COPY ./go_exporter/files/go.mod /go/src/app/go.mod
COPY ./go_exporter/files/go.sum /go/src/app/go.sum

RUN go mod download && go mod verify

RUN go build -o /go/src/app ./go_exporter


# multi stage build
# FROM alpine:latest

# COPY --from=builder /go/src/app /go/src/app

# CMD ["/go/src/app/main"]

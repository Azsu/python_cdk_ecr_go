FROM golang:1.17

WORKDIR /stack/app
COPY main.go .
RUN go build -o main

ENTRYPOINT ["/stack/app/main"]
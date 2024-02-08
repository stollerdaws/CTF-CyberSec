# Build stage for Go application
FROM golang:1.20 AS builder
WORKDIR /app
COPY src/go.mod src/go.sum ./
RUN go mod download
COPY src/*.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o myapp
# Final stage with Ubuntu and MySQL
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y mysql-server && rm -rf /var/lib/apt/lists/*

# Copy the compiled app from the builder stage
COPY --from=builder /app/myapp /myapp

# Copy static files and scripts
COPY src/web /web
COPY setup.sql /setup.sql
COPY entrypoint.sh /entrypoint.sh

# Set permissions and expose necessary port
RUN chmod +x /entrypoint.sh
EXPOSE 1337

ENTRYPOINT ["/entrypoint.sh"]

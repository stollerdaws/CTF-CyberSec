#!/bin/bash

echo "Starting MySQL..."
service mysql start

# Wait for MySQL to be ready
while ! mysqladmin ping --silent; do
    echo "Waiting for MySQL to start..."
    sleep 1
done

echo "MySQL started."

echo "Running setup.sql..."
mysql < /setup.sql

echo "Running web app..."
/myapp

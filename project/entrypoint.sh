#!/bin/sh

echo "waiting for godot..err..postgres..."

while ! nc -z web-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

exec "$@"

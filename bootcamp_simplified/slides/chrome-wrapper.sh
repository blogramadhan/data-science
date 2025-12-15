#!/usr/bin/env bash
# Wrapper to launch Chrome/Chromium with relaxed sandboxing for marp in restricted environments.
exec /usr/bin/google-chrome \
  --no-sandbox \
  --disable-setuid-sandbox \
  --disable-dev-shm-usage \
  --disable-gpu \
  --disable-crash-reporter \
  --disable-crashpad \
  "$@"

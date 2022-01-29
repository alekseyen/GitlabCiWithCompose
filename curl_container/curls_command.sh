#!/bin/bash

echo 'sleep' && sleep 10 \
   && echo curl -X 'POST' \
  'fastapi_app:8003/shorten' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": ""http://google.com"
}' && curl -X 'POST' \
  'fastapi_app:8003/shorten' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "http://google.com"
}' && echo curl -w '%{response_code}\n' -so /dev/null 'fastapi_app:8003/go/38e67108-4' && \
curl -w '%{response_code}\n' -so /dev/null 'fastapi_app:8003/go/38e67108-4'

# Simplies fast-api server

To Run app use:
```bash
cd url_shortener && uvicorn url_shortener:app --port 8003
```

POST:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/shorten' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://testurl.com"
}'
```

GET:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/go/3ad24b09-2'
```
(or just type it in browser)

To run test: 
```bash
pytest .
```

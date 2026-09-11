# Webhook Mock API

API simples para recebimento de webhooks mock.

## Endpoints

- `POST /webhook`
- `GET /webhook/total`
- `DELETE /webhook/reset`
- `GET /health`

## Run local

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
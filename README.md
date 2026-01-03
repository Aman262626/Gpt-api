# Gpt-api

Minimal Flask API compatible with the hackGPT-Ultimate Streamlit frontend.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

## Deploy (Render)

- Start command (if needed): `gunicorn app:app`
- The service will bind to `PORT` automatically.

## API

- `GET /` health check
- `POST /chat` accepts JSON with `message` or `question` and optional `meta`

Example payload:

```json
{
  "message": "Hello",
  "meta": {"persona": "DEV", "lang": "English", "depth": 5}
}
```

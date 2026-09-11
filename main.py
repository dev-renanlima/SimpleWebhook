from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from threading import Lock

app = FastAPI()

total_webhooks = 0
lock = Lock()

@app.post("/webhook")
async def webhook(request: Request):
    global total_webhooks
    await request.body()
    with lock:
        total_webhooks += 1

    return JSONResponse({
        "Success": "True",
        "Message": "SUSTENTAÇÃO DEV MERO'S - RECEBIDO",
        "StatusCode": "200"
    })

@app.get("/webhook/total")
def total():
    return {"TotalWebhooks": total_webhooks}

@app.delete("/webhook/reset")
def reset():
    global total_webhooks
    with lock:
        total_webhooks = 0
    return {"TotalWebhooks": total_webhooks}

@app.get("/health")
def health():
    return {"status": "ok"}
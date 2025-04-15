from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/webhook', status_code=202)
async def dispatch_event():
    pass

uvicorn.run(app, host='0.0.0.0', port=8080)
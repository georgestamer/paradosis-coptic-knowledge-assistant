from fastapi import FastAPI
from app.api.webhook import router
app = FastAPI(title='PARADOSIS', version='0.1.0')
app.include_router(router)
@app.get('/health')
def health(): return {'status':'ok'}

from fastapi import APIRouter, HTTPException, Query
from app.core.config import settings
router = APIRouter()
@router.get('/webhook')
def verify(mode: str=Query(alias='hub.mode'), token: str=Query(alias='hub.verify_token'), challenge: str=Query(alias='hub.challenge')):
    if mode != 'subscribe' or token != settings.whatsapp_verify_token: raise HTTPException(403, 'invalid verification')
    return int(challenge) if challenge.isdigit() else challenge
@router.post('/webhook')
async def webhook(payload: dict):
    return {'status':'accepted'}

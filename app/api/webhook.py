from fastapi import APIRouter, BackgroundTasks, HTTPException, Query
from app.core.config import settings
from app.database.connection import SessionLocal
from app.services.message_service import reply
from app.services.whatsapp_service import send_text
router = APIRouter(); processed: set[str] = set()
@router.get('/webhook')
def verify(mode: str=Query(alias='hub.mode'), token: str=Query(alias='hub.verify_token'), challenge: str=Query(alias='hub.challenge')):
    if mode != 'subscribe' or token != settings.whatsapp_verify_token: raise HTTPException(403, 'invalid verification')
    return int(challenge) if challenge.isdigit() else challenge
async def process_message(sender: str, message_id: str, text: str):
    if message_id in processed: return
    processed.add(message_id); db = SessionLocal()
    try: await send_text(sender, reply(db, text))
    finally: db.close()
@router.post('/webhook')
async def webhook(payload: dict, background_tasks: BackgroundTasks):
    for entry in payload.get('entry', []):
        for change in entry.get('changes', []):
            for message in change.get('value', {}).get('messages', []):
                if message.get('type') == 'text' and message.get('id') and message.get('from'):
                    background_tasks.add_task(process_message, message['from'], message['id'], message['text'].get('body', ''))
    return {'status':'accepted'}

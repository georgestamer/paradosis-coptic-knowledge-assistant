import httpx
from app.core.config import settings
async def send_text(to: str, text: str):
    if not settings.whatsapp_access_token or not settings.whatsapp_phone_number_id: return None
    url = f'https://graph.facebook.com/{settings.whatsapp_api_version}/{settings.whatsapp_phone_number_id}/messages'
    headers = {'Authorization': f'Bearer {settings.whatsapp_access_token}'}
    payload = {'messaging_product':'whatsapp','to':to,'type':'text','text':{'body':text}}
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

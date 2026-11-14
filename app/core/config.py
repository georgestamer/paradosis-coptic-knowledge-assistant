from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    database_url: str = 'postgresql+psycopg://paradosis:paradosis@localhost:5432/paradosis'
    whatsapp_access_token: str = ''
    whatsapp_phone_number_id: str = ''
    whatsapp_verify_token: str = ''
    whatsapp_api_version: str = 'v21.0'
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
settings = Settings()

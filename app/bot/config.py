from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TG_TOKEN: str

    model_config = SettingsConfigDict(env_file=".env")
    
settings = Settings()
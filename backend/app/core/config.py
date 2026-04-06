from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Horizon Finance Platform"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./horizon_finance.db"
    SECRET_KEY: str = "horizon-finance-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480  # 8 hours
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()

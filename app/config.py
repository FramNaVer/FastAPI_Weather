import os

class Settings:
    DB_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:Tanadon02162004@localhost:3306/WeatherApp")

settings = Settings()

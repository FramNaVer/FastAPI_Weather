from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import city  # เพิ่ม router
from app.routers import auth

app = FastAPI()

# สร้างตารางทั้งหมด (เฉพาะครั้งแรก)
Base.metadata.create_all(bind=engine)

# Register router
app.include_router(auth.router)
app.include_router(city.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Weather App"}

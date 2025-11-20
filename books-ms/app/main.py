from fastapi import FastAPI
from app.database import Base, engine
from app.routes import books
from app.events.producer import producer

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Books Microservice")

@app.on_event("startup")
async def startup():
    await producer.start()

@app.on_event("shutdown")
async def shutdown():
    await producer.stop()

app.include_router(books.router)
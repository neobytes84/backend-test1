import logging
from fastapi import FastAPI
from .database import Base, engine
from .routes import authors
from .events.producer import producer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Authors Microservice")

@app.on_event("startup")
async def startup_event():
    await producer.start()
    logging.getLogger(__name__).info("Kafka producer started")

@app.on_event("shutdown")
async def shutdown_event():
    await producer.stop()
    logging.getLogger(__name__).info("Kafka producer stopped")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(authors.router)
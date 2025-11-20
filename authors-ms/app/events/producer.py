import json
import asyncio
from aiokafka import AIOKafkaProducer
from app.config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC_AUTHOR_CREATED,
    KAFKA_TOPIC_AUTHOR_BOOK_ASSIGNED,
)

class KafkaEventProducer:
    def __init__(self):
        self._producer: AIOKafkaProducer | None = None

    async def start(self):
        self._producer = AIOKafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        await self._producer.start()

    async def stop(self):
        if self._producer:
            await self._producer.stop()

    async def send_author_created(self, author_id: int, name: str):
        payload = {"author_id": author_id, "name": name}
        await self._producer.send_and_wait(KAFKA_TOPIC_AUTHOR_CREATED, payload)

    async def send_author_book_assigned(self, author_id: int, book_id: int):
        payload = {"author_id": author_id, "book_id": book_id}
        await self._producer.send_and_wait(KAFKA_TOPIC_AUTHOR_BOOK_ASSIGNED, payload)

producer = KafkaEventProducer()

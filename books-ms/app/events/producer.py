import json
from aiokafka import AIOKafkaProducer
from app.config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC_BOOK_CREATED,
    KAFKA_TOPIC_BOOK_AUTHOR_ASSIGNED,
)

class BookKafkaProducer:
    def __init__(self):
        self._producer = None

    async def start(self):
        self._producer = AIOKafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        await self._producer.start()

    async def stop(self):
        if self._producer:
            await self._producer.stop()

    async def send_book_created(self, book_id: int, title: str):
        await self._producer.send_and_wait(
            KAFKA_TOPIC_BOOK_CREATED,
            {"book_id": book_id, "title": title}
        )

    async def send_book_author_assigned(self, book_id: int, author_id: int):
        await self._producer.send_and_wait(
            KAFKA_TOPIC_BOOK_AUTHOR_ASSIGNED,
            {"book_id": book_id, "author_id": author_id}
        )

producer = BookKafkaProducer()

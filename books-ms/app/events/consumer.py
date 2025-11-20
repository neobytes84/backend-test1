import asyncio
from aiokafka import AIOKafkaConsumer
from app.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC_BOOK_AUTHOR_ASSIGNED

async def start_consumer():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC_BOOK_AUTHOR_ASSIGNED,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="books-group",
        value_deserializer=lambda v: v.decode("utf-8")
    )

    await consumer.start()
    try:
        async for msg in consumer:
            print(f"[BOOKS] Event received → {msg.topic}: {msg.value}")
            # Lógica real iría aquí
    finally:
        await consumer.stop()

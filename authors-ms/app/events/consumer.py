import asyncio
from aiokafka import AIOKafkaConsumer
from app.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC_AUTHOR_BOOK_ASSIGNED

async def start_consumer():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC_AUTHOR_BOOK_ASSIGNED,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="authors-group",
        value_deserializer=lambda v: v.decode("utf-8")
    )

    await consumer.start()
    try:
        async for msg in consumer:
            print(f"[AUTHORS] Event received → {msg.topic}: {msg.value}")
            # Aquí iría lógica real
    finally:
        await consumer.stop()

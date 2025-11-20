from dotenv import load_dotenv
load_dotenv()

import os

DATABASE_URL = os.getenv("DATABASE_URL")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

# Topics específicos de books-ms
KAFKA_TOPIC_BOOK_CREATED = "book.created"
KAFKA_TOPIC_BOOK_AUTHOR_ASSIGNED = "book.author.assigned"

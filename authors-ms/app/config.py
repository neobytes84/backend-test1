from dotenv import load_dotenv
load_dotenv()

import os

DATABASE_URL = os.getenv("DATABASE_URL")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

# Topics específicos de authors-ms
KAFKA_TOPIC_AUTHOR_CREATED = "author.created"
KAFKA_TOPIC_AUTHOR_BOOK_ASSIGNED = "author.book.assigned"

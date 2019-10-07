# Utilities
import psycopg2
from psycopg2 import pool


threaded_postgreSQL_pool = psycopg2 \
    .pool.ThreadedConnectionPool(
        1, 
        20,
        user = "postgres",
        password = "edgar123",
        host = "127.0.0.1",
        port = "5432",
        database = "inventsoft"
)

if(threaded_postgreSQL_pool):
    print("Connection pool created successfully using ThreadedConnectionPool")
```python
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Shared variables
DB_CONNECTION = "dbname=test user=postgres password=secret"

# Shared schemas
UserSchema = {
    "email": "TEXT",
    "password": "TEXT",
    "tasks": "JSONB"
}

TaskSchema = {
    "task_id": "SERIAL PRIMARY KEY",
    "task_name": "TEXT",
    "task_time": "TIMESTAMP"
}

EmailSchema = {
    "email_id": "SERIAL PRIMARY KEY",
    "email_subject": "TEXT",
    "email_body": "TEXT",
    "email_time": "TIMESTAMP"
}

def connectDB():
    conn = psycopg2.connect(DB_CONNECTION)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return conn

def create_table(conn, table_name, schema):
    cur = conn.cursor()
    columns = ", ".join([f"{k} {v}" for k, v in schema.items()])
    create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({});").format(
        sql.Identifier(table_name), sql.SQL(columns)
    )
    cur.execute(create_table_query)
    conn.commit()
    cur.close()

def insert_data(conn, table_name, data):
    cur = conn.cursor()
    columns = ", ".join(data.keys())
    values = ", ".join(["%s"] * len(data))
    insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({});").format(
        sql.Identifier(table_name), sql.SQL(columns), sql.SQL(values)
    )
    cur.execute(insert_query, list(data.values()))
    conn.commit()
    cur.close()

def query_data(conn, table_name, condition=None):
    cur = conn.cursor()
    query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
    if condition:
        query += sql.SQL(" WHERE {}").format(sql.SQL(condition))
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows

# Initialize database and tables
conn = connectDB()
create_table(conn, "users", UserSchema)
create_table(conn, "tasks", TaskSchema)
create_table(conn, "emails", EmailSchema)
```
import os
import json
import psycopg2
from datetime import datetime

RAW_DIR = "data/raw/telegram_messages/2025-07-15"  # Adjust the date as needed

conn = psycopg2.connect(
    dbname="kara_db",
    user="your_user",
    password="your_password",
    host="localhost",
    port=5432
)

cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS raw.telegram_messages (
    id BIGINT,
    message TEXT,
    date TIMESTAMP,
    channel TEXT,
    sender_id BIGINT,
    has_media BOOLEAN,
    media_path TEXT,
    raw JSONB
);
""")
conn.commit()

for file in os.listdir(RAW_DIR):
    if file.endswith(".json"):
        channel = file.replace(".json", "")
        with open(os.path.join(RAW_DIR, file), encoding="utf-8") as f:
            data = json.load(f)
            for msg in data:
                cur.execute("""
                INSERT INTO raw.telegram_messages (
                    id, message, date, channel, sender_id, has_media, media_path, raw
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    msg.get("id"),
                    msg.get("message"),
                    msg.get("date"),
                    channel,
                    msg.get("sender_id"),
                    bool(msg.get("media")),
                    msg.get("downloaded_media_path"),
                    json.dumps(msg)
                ))
conn.commit()
cur.close()
conn.close()

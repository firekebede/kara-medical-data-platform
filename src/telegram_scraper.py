import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
from telethon.sync import TelegramClient

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME")
RAW_DATA_DIR = "data/raw/telegram_messages"
LOG_PATH = "logs/telegram_scraper.log"

CHANNELS = [
    "lobelia4cosmetics",
    "tikvahpharma",
    # Add more later
]

# Setup logging
logging.basicConfig(filename=LOG_PATH, level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

def scrape_channel(channel_name):
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(f"{RAW_DATA_DIR}/{today}", exist_ok=True)
    output_path = f"{RAW_DATA_DIR}/{today}/{channel_name}.json"

    with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        try:
            messages = client.iter_messages(channel_name, limit=1000)
            data = []
            for msg in messages:
                item = msg.to_dict()
                if msg.media:
                    media_path = f"{RAW_DATA_DIR}/{today}/{channel_name}_{msg.id}"
                    client.download_media(msg, media_path)
                    item['downloaded_media_path'] = media_path
                data.append(item)

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            logging.info(f"✅ Scraped {channel_name}, saved to {output_path}")

        except Exception as e:
            logging.error(f"❌ Failed to scrape {channel_name}: {e}")

if __name__ == "__main__":
    for channel in CHANNELS:
        scrape_channel(channel)

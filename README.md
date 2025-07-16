# Kara Medical Data Platform 

This repository contains an end-to-end data pipeline designed to analyze Ethiopian medical businesses using data scraped from public Telegram channels.

## Features

- Telegram Scraping: Extract messages and images from selected public channels.
- Data Lake: Store raw JSON data in a structured, timestamped format.
- PostgreSQL Data Warehouse: Load and store raw data for transformation.
- dbt Transformations: Clean, structure, and model data into a star schema.
- YOLOv8 Enrichment: Detect medical-related objects from images and link them to messages.
- FastAPI: Build API endpoints to expose insights and answer key business questions.
- Dagster Orchestration: Manage, run, and schedule the entire pipeline.

## Project Structure
kara-medical-data-platform/
├── data/
├── kara_dbt/
├── kara_fastapi/
├── dagster_pipeline.py
├── requirements.txt
└── README.md

diff
Copy
Edit

## API Endpoints

- GET /api/reports/top-products: Most frequently mentioned medical products
- GET /api/channels/{channel_name}/activity: Posting activity per channel
- GET /api/search/messages?query=keyword: Search messages by keyword

## Tools and Libraries

- Python, Telethon
- PostgreSQL
- dbt (Data Build Tool)
- YOLOv8 (Ultralytics)
- FastAPI, Pydantic
- Dagster (for orchestration)



from dagster import job, op

@op
def scrape_telegram_data():
    # call your telegram scraping logic/script here
    print("Scraping Telegram data...")

@op
def load_raw_to_postgres():
    # load raw JSON data to Postgres
    print("Loading raw data to Postgres...")

@op
def run_dbt_transformations():
    # run dbt transformations
    print("Running dbt transformations...")

@op
def run_yolo_enrichment():
    # run YOLO object detection on images
    print("Running YOLO enrichment...")

@job
def full_pipeline():
    scrape_telegram_data()
    load_raw_to_postgres()
    run_dbt_transformations()
    run_yolo_enrichment()


from dagster import schedule

@schedule(cron_schedule="0 0 * * *", job=full_pipeline, execution_timezone="Africa/Addis_Ababa")
def daily_run(_context):
    return {}

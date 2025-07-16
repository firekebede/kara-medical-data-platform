from sqlalchemy.orm import Session

def get_top_products(db: Session, limit: int = 10):
    query = """
        SELECT message, COUNT(*) AS mention_count
        FROM fct_messages
        WHERE message IS NOT NULL
        GROUP BY message
        ORDER BY mention_count DESC
        LIMIT :limit
    """
    return db.execute(query, {"limit": limit}).fetchall()

def get_channel_activity(db: Session, channel_name: str):
    query = """
        SELECT date, COUNT(*) as message_count
        FROM fct_messages
        WHERE channel = :channel
        GROUP BY date
        ORDER BY date
    """
    return db.execute(query, {"channel": channel_name}).fetchall()

def search_messages(db: Session, query: str):
    q = f"%{query}%"
    return db.execute(
        "SELECT id, channel, message, date FROM fct_messages WHERE message ILIKE :q",
        {"q": q}
    ).fetchall()

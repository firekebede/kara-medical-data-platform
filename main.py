from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/reports/top-products", response_model=List[schemas.TopProduct])
def top_products(limit: int = 10, db: Session = Depends(get_db)):
    results = crud.get_top_products(db, limit)
    return [{"product": r[0], "mention_count": r[1]} for r in results]

@app.get("/api/channels/{channel_name}/activity", response_model=List[schemas.ChannelActivity])
def channel_activity(channel_name: str, db: Session = Depends(get_db)):
    results = crud.get_channel_activity(db, channel_name)
    return [{"date": str(r[0]), "message_count": r[1]} for r in results]

@app.get("/api/search/messages", response_model=List[schemas.MessageResult])
def search_messages(query: str, db: Session = Depends(get_db)):
    results = crud.search_messages(db, query)
    return [
        {"id": r[0], "channel": r[1], "message": r[2], "date": str(r[3])}
        for r in results
    ]

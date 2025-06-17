from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
from typing import List
from datetime import datetime  

app = FastAPI()

entries = []

class JournalEntry(BaseModel):
    text: str

@app.post("/journal")
def add_entries(journal_data: List[JournalEntry]):
    responses = []
    for entry in journal_data:
        analysis = TextBlob(entry.text)
        score = analysis.sentiment.polarity

        if score > 0.1:
            mood = "positive"
        elif score < -0.1:
            mood = "negative"
        else:
            mood = "neutral"

        result = {
            "text": entry.text,
            "mood": mood,
            "score": round(score, 2),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        }

        entries.append(result)
        responses.append(result)

    return responses

@app.get("/stats")
def get_stats():
    stats = {
        "positive": 0,
        "neutral": 0,
        "negative": 0
    }

    for entry in entries:
        mood = entry["mood"]
        if mood in stats:
            stats[mood] += 1

    stats["total_entries"] = len(entries)
    return stats

@app.get("/entries")
def get_entries():
    return entries

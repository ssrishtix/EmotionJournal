# 🐾 Emotion Journal 📔

A **cute, mood-powered journaling app** built using **FastAPI** and **TextBlob**. Analyze your emotions through your journal entries and view your daily mood stats — like a digital scrapbook for your feelings! 🌈✨

---

## 💡 Features

- 📝 Add multiple journal entries at once
- 💬 Auto-detect mood using AI (positive, neutral, negative)
- 📊 Track your emotional stats
- 🕒 Timestamped entries
- 🌸 Frontend coming soon with pastel vibes & cute emojis!

---

## 🔧 Tech Stack

- **Backend:** FastAPI
- **NLP:** TextBlob (Sentiment Analysis)
- **Language:** Python
- **Database:** In-memory (for now – switching to persistent DB soon)
- **Frontend:** Under construction ✨

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/emotion-journal.git
cd emotion-journal

# 2. Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn main:app --reload

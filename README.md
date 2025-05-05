# 📰 Bengali News Sentiment Analyzer

A Django-based web app that takes a Bangla news website URL, extracts the latest headline, translates it into English, and performs sentiment analysis (positive, negative, or neutral).

---

## 📌 Features

- 🌐 Accepts URL of popular Bangla news websites (Prothom Alo, Kaler Kantho, BD Pratidin)
- 📰 Extracts the first headline automatically
- 🌍 Translates Bangla headline into English using Google Translate
- 🧠 Analyzes sentiment using a multilingual BERT-based model
- 🎨 Stylish and responsive Bootstrap interface

---

## 🛠 How I Built This

### Tools & Technologies

- **Backend Framework**: Django
- **Frontend**: HTML5, Bootstrap 5, Font Awesome
- **Sentiment Analysis**: [Hugging Face Transformers](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
- **Translation**: `googletrans` Python library
- **Scraping**: `requests` + `BeautifulSoup`
- **Hosting**: (Optional) Deployable on any Django-supported platform

---

## 🚀 How It Works

1. **User Input**: User submits a Bangla news URL.
2. **Scraping**: The backend fetches the HTML and parses the first headline.
3. **Translation**: The headline is translated into English.
4. **Sentiment Analysis**: The translated text is passed to a BERT model which returns a sentiment rating (1–5 stars), converted to a sentiment label.
5. **Display**: The original and translated headlines with the sentiment result are shown.

---

## 🧪 Supported News Sources

Currently supports:

- [Prothom Alo](https://www.prothomalo.com/)
- [Kaler Kantho](https://www.kalerkantho.com/)
- [BD Pratidin](https://www.bd-pratidin.com/)

Other sources will return a fallback error.

---

## 🧰 How to Run This Project Locally

### 1. Clone the Repo

```bash
git clone https://github.com/Nayemjaman/news_sentiment
cd news_sentiment
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash (For developement)
python manage.py runserver
```
```bash (For production)
uvicorn config.asgi:application --host 0.0.0.0 --port 8000
```

---

Open your browser and go to:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📦 Requirements

Sample `requirements.txt`:

```
Django>=4.0
transformers
torch
googletrans==4.0.0rc1
beautifulsoup4
requests
```

---

## 👨‍💻 Author

Built with ❤️ by Md. Nayem Jaman Tusher
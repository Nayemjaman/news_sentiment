# newsapp/sentiment.py

from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text):
    try:
        result = classifier(text)[0]
        label = result['label']

        stars = int(label.split()[0])
        print(stars)
        if stars <= 2:
            return "negative"
        elif stars == 3:
            return "neutral"
        else:
            return "positive"
    except Exception as e:
        return f"Error analyzing sentiment: {str(e)}"

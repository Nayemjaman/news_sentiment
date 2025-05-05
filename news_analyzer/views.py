
from django.shortcuts import render
from datetime import datetime
from news_analyzer.analysis import analyze_sentiment
from news_analyzer.translate import translate_to_english
from .forms import URLInputForm
from .scraper import get_first_headline

def index(request):
    headline = None
    english_headline = None
    sentiment = None
    if request.method == 'POST':
        form = URLInputForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['newspaper_url']
            headline = get_first_headline(url)
            english_headline = translate_to_english(headline)
            sentiment = analyze_sentiment(english_headline)
    else:
        form = URLInputForm()
    
    return render(request, 'index.html', {
        'form': form, 'headline': headline, 
        'english_headline': english_headline,
        'sentiment': sentiment,
        'year': datetime.now().year,
        })

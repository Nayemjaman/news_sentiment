
from django.shortcuts import render
from .forms import URLInputForm
from .scraper import get_first_headline

def index(request):
    headline = None
    if request.method == 'POST':
        form = URLInputForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['newspaper_url']
            headline = get_first_headline(url)
    else:
        form = URLInputForm()
    
    return render(request, 'index.html', {'form': form, 'headline': headline})

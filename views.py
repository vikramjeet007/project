from django.shortcuts import render
from forms import ContactForm


def contact(request):
    form = ContactForm()
    return render(request, '../templates/index.html', {'form': form})

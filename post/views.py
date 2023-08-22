from django.shortcuts import render

# Create your views here.
# MVT


def index(request):
    return render(request, 'index.html')
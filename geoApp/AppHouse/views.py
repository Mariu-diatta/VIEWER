from django.shortcuts import render
def index(request): # < here
    return render(request, 'AppHouse/index.html')

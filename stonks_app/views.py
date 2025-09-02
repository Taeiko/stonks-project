from django.shortcuts import render

# Create your views here.
# these are the pages that get displayed when the user types the url
def welcome(request):
    return render(request, 'welcome.html')
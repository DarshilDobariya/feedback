from django.http import HttpResponse
from django.shortcuts import render

from app.models import FeedBack

# Create your views here.
def index(request):
    return render(request, 'index.html')

def feedback(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        feedback = request.POST["feedback"]
        object = FeedBack (name = name, email = email,feedback = feedback)
        object.save()
        return HttpResponse("<h1>feedback submitted</h1>")

    return render(request, 'feedback.html')
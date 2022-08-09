from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,"index.html")
def reviews(request):
    return render(request,"reviews.html")
def services(request):
    return render(request,"services.html")
def branches(request):
    return render(request,"branches.html")
def reachus(request):
    return render(request,"reachus.html")
def payment(request):
    return render(request,"payment.html")

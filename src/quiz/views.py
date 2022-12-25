from django.shortcuts import render

# Create your views here.
def quiz(request):
  return render(request, 'base.html')

def oxtc (request):
  return render(request, 'ox.html')
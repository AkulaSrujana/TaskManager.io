
# Create your views here.
from django.shortcuts import render


def main_view(request):
    return render(request, 'tasks/main.html')
    
    

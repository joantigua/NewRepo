from django.shortcuts import render
from .forms import *

# Create your views here.

def home(request):
    form = SalaryForm()
    return render(request,'calculator/index.html', {'form' : form})
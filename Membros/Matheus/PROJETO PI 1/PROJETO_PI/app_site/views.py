from django.shortcuts import render

def home(request):
    return render(request,'ProjetoPI/home.html')
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<script>document.location.href='/dashboard/'</script>")

def dashboard(request):
    return render(request,'dashboard.html', {'page': 'DASHBOARD'})

def register(request):
    return render(request,'register.html', {'page': 'REGISTER'})
 
def update(request, id):
    return render(request,'update.html', {"id": id}) 
from django.shortcuts import render
from django.http import HttpResponse
from api.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return HttpResponse("<script>document.location.href='/dashboard/'</script>")

@login_required
def dashboard(request):
    products = Product.objects.all()
    productsByMaintenance = Product.objects.exclude(maintenance__isnull=True).order_by("maintenance")[:10]
    
    return render(request,'dashboard.html', {'page': 'DASHBOAR', 'products': products, 'productsByMaintenance': productsByMaintenance})

@login_required
def register(request):
    return render(request,'register.html', {'page': 'REGISTER'})

@login_required
def update(request, id):
    return render(request,'update.html', {"id": id}) 

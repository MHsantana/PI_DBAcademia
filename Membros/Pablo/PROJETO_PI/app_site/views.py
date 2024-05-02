from django.shortcuts import render
from django.http import HttpResponse
from api.models import Product

def home(request):
    return HttpResponse("<script>document.location.href='/dashboard/'</script>")

def dashboard(request):
    products = Product.objects.all()
    productsByMaintenance = Product.objects.exclude(maintenance__isnull=True).order_by("maintenance")[:10]
    
    return render(request,'dashboard.html', {'page': 'DASHBOAR', 'products': products, 'productsByMaintenance': productsByMaintenance})

def register(request):
    return render(request,'register.html', {'page': 'REGISTER'})
 
def update(request, id):
    return render(request,'update.html', {"id": id}) 
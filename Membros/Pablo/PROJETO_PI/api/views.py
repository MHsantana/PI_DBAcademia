from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product
from .forms import ProductRegister

# Create your views here.
@csrf_exempt
def apiProducts(request):
    if request.method == "POST":
        form = ProductRegister(request.POST)
        print(request.POST)
        print(form.errors)

        if form.is_valid():
            register = form.save()
            return redirect("/dashboard/")

        return JsonResponse({'error': 'form not valid'})

    if request.method == "GET":
        products = Product.objects.all()
        responseJson = list(products.values())
        return JsonResponse(responseJson ,safe=False)
    
    return JsonResponse({'error': 'request method not valid'})

#visualiza um especifico, atualiza e deleta
@csrf_exempt
def apiProduct(request, id):

    # este atualiza um produto especifico pelo id e pelo formulario enviado
    if request.method == "POST":
        print(request.POST)
        product = Product.objects.get(id=id)

        product.name = request.POST.get('name')
        product.company = request.POST.get('company')
        product.cnpj = request.POST.get('cnpj')
        product.headquarter = request.POST.get('headquarter')
        product.email = request.POST.get('email')
        product.tel = request.POST.get('tel')
        product.tel2 = request.POST.get('tel2')
        product.branch = request.POST.get('branch').capitalize()
        product.maintenance = request.POST.get('maintenance')
        
        product.save()

        return JsonResponse({'msg': 'update id: '+id})

    # este deleta um produto especifico pelo id
    if request.method == "DELETE":
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return JsonResponse({'msg': 'deleted id: '+id})
        except:
            return JsonResponse({'error': 'id not found'})

    # este visualiza um produto especifico pelo id
    if request.method == "GET":
        try:
            product = Product.objects.get(id=id)
            responseJson = json.loads(serializers.serialize('json', [product]))
            print(responseJson[0])
            return JsonResponse(responseJson[0]['fields'], safe=False)
        except:
            return JsonResponse({'error': 'id not found'})

    return JsonResponse({'error': 'request method not valid'})
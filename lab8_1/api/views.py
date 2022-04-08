from django.http.response import HttpResponse, JsonResponse
from api.models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    print(categories_json)
    return JsonResponse(categories_json, safe=False)

def category_dateil(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(category.to_json())

def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    print(products_json)
    return JsonResponse(products_json, safe=False)

def product_dateil(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(product.to_json())

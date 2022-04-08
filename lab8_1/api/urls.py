from django.urls import path, re_path

from api.views import category_list, category_dateil, product_list, product_dateil

urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_dateil),
    path('products/', product_list),
    path('products/<int:product_id>/', product_dateil),
]
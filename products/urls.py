from django.urls import include, path
from . import views

from .models import Product

urlpatterns = [
    path('', views.products, name='products'),
    # path('send_order/', views.send_order, name='send_order'),
    path('create/', views.create, name='products_create'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
    path('category/<category>/', views.product_category, name="product_category"),
    path('brand/<str:contributor>/', views.brand, name='brand'),
    path('brand/<str:contributor>/<str:category>/', views.brand_product_category, name="brand_product_category"),
    path('brand/<str:contributor>/landing', views.brand_landing, name="brand_landing"),
    path('brand/<str:contributor>/select', views.brand_select, name="brand_select"),
    path('brand/<str:contributor>/review', views.brand_review, name="brand_review")
]

from django.urls import path
from .views import ProductListView, ProductDetailView
from .views import home
from .views import post_list



urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('', home, name='home'),
    path("posts/", post_list, name="post_list"),
]

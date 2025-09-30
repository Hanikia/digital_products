from django.urls import path
from .views import( ProductListView, ProductDetailView,
      CategoryListView, CategoryDetailView, FileListView,
      FileDetailView             
)
from .views import home
from .views import post_list



urlpatterns = [
    path('categories/', CategoryListView.as_view(), name = 'category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:product_id>/files/', FileListView.as_view(), name='files'),
    path('products/<int:product_id>/files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('', home, name='home'),
    path("posts/", post_list, name="post_list"),
]

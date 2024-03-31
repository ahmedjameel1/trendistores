from django.urls import path
from . import views 

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('product/<str:pk>/',
         views.ProductDetailView.as_view(), name='product'),
]

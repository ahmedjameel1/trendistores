from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'products', ProductViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]

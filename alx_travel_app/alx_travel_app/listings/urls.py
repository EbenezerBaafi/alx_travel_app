from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'listings'

router = DefaultRouter()
# Add your viewsets here when you create them
# router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from .views import test_api, test_api_with_auth, create_user_with_api

urlpatterns = [
    path('test_api/', test_api),
    path('test_api_auth/', test_api_with_auth),
    path('test_api_perm/', create_user_with_api),
]

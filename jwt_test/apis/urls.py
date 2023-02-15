from django.urls import path, include
from .views import test_api, test_api_with_auth, test_api_with_perm, create_user_with_api, delete_user_with_api, change_user_group_with_api

urlpatterns = [
    path('test_api/', test_api),
    path('test_api_auth/', test_api_with_auth),
    path('test_api_perm/', test_api_with_perm),
    path('create_user/', create_user_with_api),
    path('delete_user/', delete_user_with_api),
    path('change_user_group/', change_user_group_with_api),
]

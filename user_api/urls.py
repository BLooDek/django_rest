from django.urls import include, path
from . import  views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('valid/<str:email>', views.user_exist)
]

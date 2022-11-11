from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.get_all),
    path('<int:id>/', views.note),
    path('get_all_all', views.get_all_all)
]

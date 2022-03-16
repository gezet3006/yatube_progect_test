from django.urls import path
from . import views


app_name = 'yatube_test'

urlpatterns = [
    path('', views.index, name = 'glav'),
    # Страницы сообществ 
    path('group/<slug:slug>/', views.group_list, name = 'groups'),
]
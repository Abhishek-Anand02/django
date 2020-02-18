from django.urls import path
from . import views
urlpatterns = [
    path('',views.base, name = "base"),
    path('detail', views.detail,name = "detail"),
    path('result',views.result,name = "result")
]
from django.urls import path
from . import views

urlpatterns = [
    path ('', views.homepage, name="homepage"),
    path ('create/', views.create, name="create"),
    path ('<slug:slug>/', views.homepage),
    path ('<slug:slug>/results/', views.results)
]

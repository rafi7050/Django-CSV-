from django.urls import path
from . import views

app_name = "core"   


urlpatterns = [
    path("homepage", views.homepage, name="homepage"), 
    path("", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("upload", views.simple_upload, name="upload"),

]
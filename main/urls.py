from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),  # pointing to the main view
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    url(r'^captcha/', include('captcha.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
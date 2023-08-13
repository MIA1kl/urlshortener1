from django.urls import path
from . import views
app_name = "url"


urlpatterns = [
    path('', views.urlShort),
    path('<str:shorturl>', views.urlRedirect),
]
from django.urls import path, include

from . import views

app_name = "llamadas"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("__reload__/", include("django_browser_reload.urls")),
]
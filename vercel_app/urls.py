from django.contrib import admin
from django.urls import path, include

app_name='encuestas'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('encuestas.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

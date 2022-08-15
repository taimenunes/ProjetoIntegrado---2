from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Schedule.urls')),
    path('Usuarios/', include('Usuarios.urls')),
    path('admin/', admin.site.urls),
]

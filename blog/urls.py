from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', indexx),
    path('malibu/', malibuu),
    path('about/', AboutView.as_view())
]

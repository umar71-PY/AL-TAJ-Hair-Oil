from django.contrib import admin
from django.urls import path, include # include laazmi add karna

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')), # Store app ko connect kar diya
]
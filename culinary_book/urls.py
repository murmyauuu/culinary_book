from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),  
    path('recipes/', include('recipes.urls')),
    path('', RedirectView.as_view(url='/recipes/')),
    path('accounts/register/', views.register, name='register'),
]
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('register/', include('register_n_profile.urls'), name='register_n_profile'),
]

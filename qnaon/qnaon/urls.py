from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('main.urls'), name='home'),
    path('admin/', admin.site.urls),

    path('register/', include('register_n_profile.urls'), name='register_n_profile'),
]

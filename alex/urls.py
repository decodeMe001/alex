from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('home/', include('dashboard.urls', namespace='home')),
    path('chat/', include('alexchat.urls', namespace='roomchat')),
    path('api/', include('bankbranch.urls')),
    path('access/alex-d-chatbot/admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

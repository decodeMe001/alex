from django.urls import include, path

from . import views

app_name = "roomchat"

urlpatterns = [
    path('room-chat/', views.index, name='index')
]
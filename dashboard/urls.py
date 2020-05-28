from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('polls/', views.get_polls, name="polls"),
    # polls/details/1/
    path('details/<int:poll_id>/', views.poll_detail, name='detail'),
    # polls/details/1/opinion
    path('details/<int:poll_id>/opinion/', views.poll_opinion, name='opinion'),
    #logout
    path('logout/', views.logout_user, name='logout')
]
from django.urls import path
from  . import views
urlpatterns = [
    path('', views.board , name="leader board"),
    path('quit', views.quit, name="Quit")
]
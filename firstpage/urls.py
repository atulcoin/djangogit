from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='calculations'),
    path('viewdatabase', views.viewdatabase, name='viewdatabase'),
    path('updatedata', views.updatedata, name='updatedata')

]
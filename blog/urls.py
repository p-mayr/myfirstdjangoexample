from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.header, name='header'),
    url(r'^posts/', views.posts, name='posts'),
    url(r'^charts/', views.charts, name='charts'),
    url(r'^home/', views.home, name='home'),

]
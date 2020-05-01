from django.contrib import admin
from django.urls import path

from stocksbasic import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^$', views.home, name='home'),
    path(r'^stocks/(\d+)/', views.stock_details, name='stock_details'),
]

from django.contrib import admin
from django.urls import path

from stocksbasic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('stock/<int:id>/', views.stock_details, name='stock_details'),
]

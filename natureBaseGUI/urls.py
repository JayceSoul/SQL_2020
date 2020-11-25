from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Welcome'),
    path('<int:input_id>/', views.pathing, name='test'),
]
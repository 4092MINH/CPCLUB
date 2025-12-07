from django.urls import path
from . import views
urlpatterns = [
    path('', views.members),
    path('detail/<int:member_id>/', views.detail, name='member_detail'),
]
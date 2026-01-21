from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/add/', views.add_post, name='add_post'),
    path('comment/add/<int:post_id>/', views.add_comment, name='add_comment'),
]

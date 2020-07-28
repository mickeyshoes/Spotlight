from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:movie_id>', views.detail, name="detail"),
    path('like/<int:comment_id>', views.like, name="like"),
    path('cancel/<int:comment_id>', views.cancel, name="cancel"),
    path('new/<int:movie_id>', views.new, name="new"),
    path('delete', views.delete, name="delete"),
]

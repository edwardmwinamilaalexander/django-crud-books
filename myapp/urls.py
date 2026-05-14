from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.detail, name='detail'),
    path('add/', views.add_book, name='add_book'),
    path('book/<int:book_id>/edit/', views.update, name='update'),
    path('book/<int:book_id>/delete/', views.delete, name='delete'),
]

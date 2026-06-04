from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox_view, name='inbox'),
    path('outbox/', views.outbox_view, name='outbox'),
    path('archive/', views.archive_view, name='archive'),
    path('trash/', views.trash_view, name='trash'),
    path('compose/', views.compose_view, name='compose'),
    path('email/<int:message_id>/', views.detail_view, name='detail'),
    path('email/<int:message_id>/move/<str:new_folder>/', views.move_view, name='move'),
    path('email/<int:message_id>/delete/', views.delete_view, name='delete'),
]
from django.urls import path
from .import views
app_name = 'item'
urlpatterns = [
    path('browse/',views.browse,name = 'browse'),
    path('<int:pk>/',views.detail,name = 'detail'),
    path('newItem/',views.newItem,name = 'newItem'),
    path('<int:pk>/delete',views.delete,name = 'delete'),
    path('<int:pk>/edit',views.editItem,name = 'edit'),
]

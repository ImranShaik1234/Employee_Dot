from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee_new', views.employee_new, name='employee_new'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]

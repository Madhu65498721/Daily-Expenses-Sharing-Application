from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('users/', views.user_list, name='user_list'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expense/<int:pk>/', views.expense_detail, name='expense_detail'),
    path('download_balance_sheet/', views.download_balance_sheet, name='download_balance_sheet'),
]

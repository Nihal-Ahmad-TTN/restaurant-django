from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', manager_login, name="manager_login"),
    path('menu/', show_menu, name="show_menu"),
    path('add_menu/', add_menu, name="add_menu"),
    path('update_menu/', update_menu, name="update_menu"),
    path('update_menu/<int:menu_id>', update_item, name="update_item"),
    path('customer_orders/', customer_orders, name="customer_orders"),
    path('update_order/<str:id>/', update_order, name="update_order"),
]

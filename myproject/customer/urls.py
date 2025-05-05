from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="homepage"),
    path('home/', register, name="home"),
    path('login/', login_view, name='customer_login'),
    path('order/', order_food, name='order_food'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/remove/<str:food_id>', remove_item, name='remove_item'),
    path('cart/add/<str:food_id>/', add_to_cart, name='add_to_cart'),
    path('cart/update/<str:food_id>/', update_cart, name='update_cart'),
    path('cart/remove/<str:food_id>/', remove_item, name='remove_item'),
    path('thankyou/', thank_you, name='thank_you'),
    path('customer/dashboard/', customer_dashboard, name = 'customer_dashboard'),
    path('customer_logout/', LogoutView.as_view(), name = 'customer_logout'),
]

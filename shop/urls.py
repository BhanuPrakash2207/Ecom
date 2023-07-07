from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='aboutus'),
    path('order/',views.order,name='order'),
    path('contact/',views.contact,name='contact'),
    path('track/',views.track,name='trackhere'),
    path('cart/',views.cart,name='cart'),
    path('products/<int:myid>',views.productView,name='Product Information'),
]

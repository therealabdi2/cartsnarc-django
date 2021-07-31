from django.urls import path

from . import views

urlpatterns = [
    path('place-order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('payments/<orderId>/', views.payments, name='paymentsId'),
    path('order_complete/<orderId>/', views.order_complete, name='order_complete')
]

from django.urls import path
from . import views

from .models import OrderItem , VendorItems, Vendor, Item

urlpatterns = [

    path('OrderItem/', views.OrderItemList.as_view(), name="order_Item_list"),
    path('vendorItems/', views.VendorItemsList.as_view(), name='vendorItems_list'),
    path('vendor/', views.VendorList.as_view(), name='vendor_list'),
    path('item/', views.ItemList.as_view(), name='item_list'),
    path('<int:pk>/CreateOrderItem/', views.CreateOrderItem.as_view(), name='Create_Order_item'),
    path('CreateVendorItem', views.CreateVendorItem.as_view()),
    path('CreateVendor', views.CreateVendor.as_view()),
    path('CreateItem', views.CreateItem.as_view()),
    path('OrderList',views.OrderList.as_view()),
    path('createOrder',views.CreateOrder.as_view()),
    path('<pk>/deleteOrder',views.DeleteOrder.as_view(),name='deleteOrder'),
    path('<pk>/updateOrder',views.UpdateOrder.as_view(),name='updateOrder'),
    path('<pk>/deleteOrderItem', views.DeleteOrderItem.as_view(), name='deleteOrderItem'),
    path('<pk>/updateOrderItem', views.UpdateOrderItem.as_view(), name='updateOrderItem'),
    path('<pk>/deleteVendorItems', views.DeleteVendorItem.as_view(), name='deleteVendorItems'),
    path('<pk>/updateVendorItems', views.UpdateVendorItem.as_view(), name='updateVendorItems'),
    path('<pk>/deleteVendor', views.DeleteVendor.as_view(), name='deleteVendor'),
    path('<pk>/updateVendor', views.UpdateVendor.as_view(), name='updateVendor'),
    path('<pk>/deleteItem', views.DeleteItem.as_view(), name='deleteItem'),
    path('<pk>/updateItem', views.UpdateItem.as_view(), name='updateItem'),
    path('<pk>/ff',views.Test.as_view(),name='test'),
    path('<pk>/CreateTest',views.CreateTest.as_view())

]

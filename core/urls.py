from django.urls import path
from .views import *

from .models import Order , VendorItems, Vendor, Item

urlpatterns = [

    path('OrderItem/', OrderItemList.as_view(), name="order_Item_list"),
    path('vendorItems/', VendorItemsList.as_view(), name='vendorItems_list'),
    path('vendor/', VendorList.as_view(), name='vendor_list'),
    path('item/', ItemList.as_view(), name='item_list'),
    path('<pk>/CreateOrderItem/', CreateOrderItem.as_view(), name='Create_Order_item'),
    path('CreateVendorItem', CreateVendorItem.as_view()),
    path('CreateVendor', CreateVendor.as_view()),
    path('CreateItem', CreateItem.as_view()),
    path('LlList',LlList.as_view()),
    path('createOrder',CreateLl.as_view()),
    path('<pk>/deleteLl',DeleteLl.as_view(),name='deleteLl'),
    path('<pk>/updateLl',UpdateLl.as_view(),name='updateLl'),
    path('<pk>/deleteOrderItem', DeleteOrderItem.as_view(), name='deleteOrderItem'),
    path('<pk>/updateOrderItem', UpdateOrderItem.as_view(), name='updateOrderItem'),
    path('<pk>/deleteVendorItems', DeleteVendorItem.as_view(), name='deleteVendorItems'),
    path('<pk>/updateVendorItems', UpdateVendorItem.as_view(), name='updateVendorItems'),
    path('<pk>/deleteVendor', DeleteVendor.as_view(), name='deleteVendor'),
    path('<pk>/updateVendor', UpdateVendor.as_view(), name='updateVendor'),
    path('<pk>/deleteItem', DeleteItem.as_view(), name='deleteItem'),
    path('<pk>/updateItem', UpdateItem.as_view(), name='updateItem'),
    path('<pk>/ff',Test.as_view(),name='test'),
    path('<pk>/CreateTest',CreateTest.as_view())

]

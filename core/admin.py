from django.contrib import admin
from .models import Orderitem, VendorItems, Vendor, Item, Order

admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(Item)
admin.site.register(Vendor)
admin.site.register(VendorItems)

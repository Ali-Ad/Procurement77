from django.contrib import admin
from .models import Order, VendorItems, Vendor, Item, Ll

admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Vendor)
admin.site.register(VendorItems)
admin.site.register(Ll)

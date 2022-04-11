from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Order(models.Model):
    name = models.CharField(max_length=64)
    orderitem = models.ManyToManyField('Orderitem', through='Orderitem_order', related_name='+')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_created_Order", null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_updated_Order", null=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_approved_Order", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'order'


class Orderitem(models.Model):
    name = models.CharField(max_length=64)
    total_Price = models.FloatField(default="0", null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_created_Orderitem", null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_updated_Orderitem", null=True)
    vendorItems = models.ForeignKey('VendorItems', on_delete=models.CASCADE, related_name="hellof", null=True)
    quantity = models.IntegerField()
    order = models.ManyToManyField(Order, related_name='+')

    def __str__(self):
        return self.name

    @property
    def some_name(self):
        x = self.quantity * self.vendorItems.price
        return x


class Item(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_created_item")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_updated_item", null=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=64, unique=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_created_vendor", null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_updated_vendor", null=True)

    def __str__(self):
        return self.name


class VendorItems(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="vendor_VendorItem", default="",
                               null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_vendoritems", default="", null=True)
    price = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_created_vendoritems", null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_updated_vendoritems", null=True)

    def __str__(self):
        return self.item.name

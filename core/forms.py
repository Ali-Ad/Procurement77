from django import forms
from django.forms import modelformset_factory

from .models import *


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'Lls','vendorItems', 'quantity']


OrderFormset = modelformset_factory(Order, fields=('vendorItems', 'quantity'), extra=1)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'type']


class LlForm(forms.ModelForm):
    class Meta:
        model = Ll
        fields = ['name' , 'order']



LlFormset = modelformset_factory(Ll, fields=('name', 'order'), extra=1)



class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'phone', 'email', 'address']


class VendorItemsForm(forms.ModelForm):
    class Meta:
        model = VendorItems
        fields = ['vendor', 'item', 'price']

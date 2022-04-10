from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import *
from django.views.generic.base import TemplateView
from .forms import *


class Test(DetailView):
    model = Ll
    context_object_name = 'Lls'
    template_name = 'file.html'

class CreateTest(CreateView):
    model = Order
    fields = ['name', 'Lls', 'vendorItems', 'quantity']
    template_name = 'createOrder.html'
    success_url = '/core/LlList'

    def get_context_data(self, **kwargs):
        context = super(CreateOrderItem, self).get_context_data(**kwargs)
        context['formset'] = OrderFormset(queryset=Order.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        formset = OrderFormset(request.POST)

        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        instances = formset.save(commit=True)
        for instance in instances:
            instance.created_by = self.request.user
            instance.save()
        return HttpResponseRedirect('/core/LlList')

# ll
class LlList(ListView):
    model = Ll
    context_object_name = 'Lls'
    template_name = 'LlList.html'


class CreateLl(CreateView):
    model = Ll
    fields = ['name', 'order']
    template_name = 'createLl.html'
    success_url = '/core/LlList'

    def get_context_data(self, **kwargs):
        context = super(CreateLl, self).get_context_data(**kwargs)
        context['formset'] = LlFormset(queryset=Ll.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        formset = LlFormset(request.POST)

        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = self.request.user
            instance.save()
        return HttpResponseRedirect('/core/LlList')


class DeleteLl(DeleteView):
    model = Ll
    template_name = 'Delete.html'
    success_url = '/core/LlList'


class UpdateLl(UpdateView):
    model = Ll
    template_name = 'Update.html'
    success_url = '/core/LlList'
    form_class = LlForm


# Orders
class OrderItemList(ListView):
    model = Order
    context_object_name = 'Orders'
    template_name = 'OrderItemList.html.'


class CreateOrderItem(CreateView):
    model = Order
    fields = ['name', 'Lls', 'vendorItems', 'quantity']
    template_name = 'createOrder.html'
    success_url = '/core/LlList'

    def get_context_data(self, **kwargs):
        context = super(CreateOrderItem, self).get_context_data(**kwargs)
        context['formset'] = OrderFormset(queryset=Order.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        formset = OrderFormset(request.POST)

        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        instances = formset.save(commit=True)
        for instance in instances:
            instance.created_by = self.request.user
            instance.save()
        return HttpResponseRedirect('/core/LlList')

    #
    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)


class DeleteOrderItem(DeleteView):
    model = Order
    template_name = 'Delete.html'
    success_url = '/core/OrderItem'


class UpdateOrderItem(UpdateView):
    model = Order
    template_name = 'Update.html'
    form_class = OrderItemForm
    success_url = '/core/OrderItem'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# VendorItem
class VendorItemsList(ListView):
    model = VendorItems
    context_object_name = 'vendorItems'
    template_name = 'VendorItems.html'


class CreateVendorItem(CreateView):
    model = VendorItems
    fields = ['vendor', 'item', 'price']
    template_name = 'create.html'
    success_url = '/core/vendorItems'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DeleteVendorItem(DeleteView):
    model = VendorItems
    template_name = 'Delete.html'
    success_url = '/core/vendorItems'


class UpdateVendorItem(UpdateView):
    model = VendorItems
    template_name = 'Update.html'
    form_class = VendorItemsForm
    success_url = '/core/vendorItems'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# Vendor
class VendorList(ListView):
    model = Vendor
    context_object_name = 'vendors'
    template_name = 'vendor.html'


class CreateVendor(CreateView):
    model = Vendor
    fields = ['name', 'phone', 'email', 'address']
    template_name = 'create.html'
    success_url = '/core/vendor'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DeleteVendor(DeleteView):
    model = Vendor
    template_name = 'Delete.html'
    success_url = '/core/vendor'


class UpdateVendor(UpdateView):
    model = Vendor
    template_name = 'Update.html'
    form_class = VendorForm
    success_url = '/core/vendor'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# Item
class ItemList(ListView):
    model = Item
    context_object_name = 'Items'
    template_name = 'ItemList.html'


class CreateItem(CreateView):
    model = Item
    fields = ['name', 'type']
    template_name = 'create.html'
    success_url = '/core/item'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DeleteItem(DeleteView):
    model = Item
    template_name = 'Delete.html'
    success_url = '/core/item'


class UpdateItem(UpdateView):
    model = Item
    template_name = 'Update.html'
    form_class = ItemForm
    success_url = '/core/item'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class HomePageView(TemplateView):
    template_name = "account/home.html"

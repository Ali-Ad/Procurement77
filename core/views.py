from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from . import models
from django.views.generic.base import TemplateView
from . import forms


class Test(DetailView):
    model = models.Order
    context_object_name = 'Orders'
    template_name = 'file.html'


class CreateTest(CreateView):
    model = models.OrderItem
    fields = ['name', 'order', 'vendor_items', 'quantity']
    template_name = 'create_order_item.html'
    success_url = '/core/OrderList'

    def get_context_data(self, **kwargs):
        context = super(CreateTest, self).get_context_data(**kwargs)
        context['formset'] = forms.OrderItemFormset(queryset=models.OrderItem.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        formset = forms.OrderItemFormset(request.POST)

        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        instances = formset.save(commit=True)
        for instance in instances:
            instance.created_by = self.request.user

            instance.save()
        return HttpResponseRedirect('/core/OrderList')


# Order
class OrderList(ListView):
    model = models.Order
    context_object_name = 'Orders'
    template_name = 'order_list.html'


class CreateOrder(CreateView):
    model = models.Order
    fields = ['name', 'order_item']
    template_name = 'create_order.html'
    success_url = '/core/OrderList'

    def get_context_data(self, **kwargs):
        context = super(CreateOrder, self).get_context_data(**kwargs)
        context['formset'] = forms.OrderFormset(queryset=models.Order.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        formset = forms.OrderFormset(request.POST)

        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        instances = formset.save(commit=True)
        for instance in instances:
            instance.created_by = self.request.user
            instance.save()
        return HttpResponseRedirect('/core/OrderList')


class DeleteOrder(DeleteView):
    model = models.Order
    template_name = 'delete.html'
    success_url = '/core/OrderList'


class UpdateOrder(UpdateView):
    model = models.Order
    template_name = 'update.html'
    success_url = '/core/OrderList'
    form_class = forms.OrderForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# Order Item
class OrderItemList(ListView):
    model = models.OrderItem
    context_object_name = 'Orders'
    template_name = 'order_item_list.html'


class CreateOrderItem(CreateView):
    model = models.OrderItem
    fields = ['name', 'order', 'vendor_items', 'quantity']
    template_name = 'create_order_item.html'
    success_url = '/core/OrderList'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = forms.OrderItemFormset(queryset=models.OrderItem.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        formset = forms.OrderItemFormset(request.POST)

        if formset.is_valid():
            return self.form_valid(formset)

    def get_success_url(self, **kwargs):
        return reverse_lazy('Create_Order_item', args=[int(self.kwargs['pk'])])

    def form_valid(self, formset, **kwargs):
        instances = formset.save(commit=True)
        order = models.Order.objects.get(id=self.kwargs['pk'])
        for instance in instances:
            instance.created_by = self.request.user
            instance.order.add(order.id)
            instance.save()
        return super().form_valid(formset)


class DeleteOrderItem(DeleteView):
    model = models.OrderItem
    template_name = 'delete.html'
    success_url = '/core/OrderList'


class UpdateOrderItem(UpdateView):
    model = models.OrderItem
    template_name = 'update.html'
    form_class = forms.OrderItemForm
    success_url = '/core/OrderList'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# VendorItem
class VendorItemsList(ListView):
    model = models.VendorItems
    context_object_name = 'vendorItems'
    template_name = 'vendor_items.html'


class CreateVendorItem(CreateView):
    model = models.VendorItems
    fields = ['vendor', 'item', 'price']
    template_name = 'create.html'
    success_url = '/core/vendorItems'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DeleteVendorItem(DeleteView):
    model = models.VendorItems
    template_name = 'delete.html'
    success_url = '/core/vendorItems'


class UpdateVendorItem(UpdateView):
    model = models.VendorItems
    template_name = 'update.html'
    form_class = forms.VendorItemsForm
    success_url = '/core/vendorItems'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# Vendor
class VendorList(ListView):
    model = models.Vendor
    context_object_name = 'vendors'
    template_name = 'vendor.html'


class CreateVendor(CreateView):
    model = models.Vendor
    fields = ['name', 'phone', 'email', 'address']
    template_name = 'create.html'
    success_url = '/core/vendor'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DeleteVendor(DeleteView):
    model = models.Vendor
    template_name = 'delete.html'
    success_url = '/core/vendor'


class UpdateVendor(UpdateView):
    model = models.Vendor
    template_name = 'update.html'
    form_class = forms.VendorForm
    success_url = '/core/vendor'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# Item
class ItemList(ListView):
    model = models.Item
    context_object_name = 'Items'
    template_name = 'item_list.html'


class CreateItem(CreateView):
    model = models.Item
    fields = ['name', 'type']
    template_name = 'create.html'
    success_url = '/core/item'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DeleteItem(DeleteView):
    model = models.Item
    template_name = 'delete.html'
    success_url = '/core/item'


class UpdateItem(UpdateView):
    model = models.Item
    template_name = 'update.html'
    form_class = forms.ItemForm
    success_url = '/core/item'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class HomePageView(TemplateView):
    template_name = 'account/home.html'

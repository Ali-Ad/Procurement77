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
    model = models.Orderitem
    fields = ['name', 'order', 'vendorItems', 'quantity']
    template_name = 'createOrderItem.html'
    success_url = '/core/OrderList'

    def get_context_data(self, **kwargs):
        context = super(CreateTest, self).get_context_data(**kwargs)
        context['formset'] = forms.OrderItemFormset(queryset=models.Orderitem.objects.none())
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


# ll
class OrderList(ListView):
    model = models.Order
    context_object_name = 'Orders'
    template_name = 'OrderList.html'


class CreateOrder(CreateView):
    model = models.Order
    fields = ['name', 'orderitem']
    template_name = 'createLl.html'
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
    template_name = 'Delete.html'
    success_url = '/core/OrderList'


class UpdateOrder(UpdateView):
    model = models.Order
    template_name = 'Update.html'
    success_url = '/core/OrderList'
    form_class = forms.OrderForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# Orders
class OrderItemList(ListView):
    model = models.Orderitem
    context_object_name = 'Orders'
    template_name = 'OrderItemList.html'


class CreateOrderItem(CreateView):
    model = models.Orderitem
    fields = ['name', 'order', 'vendorItems', 'quantity']
    template_name = 'createOrderItem.html'
    success_url = '/core/OrderList'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = forms.OrderItemFormset(queryset=models.Orderitem.objects.none())
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
    model = models.Orderitem
    template_name = 'Delete.html'
    success_url = '/core/OrderItem'


class UpdateOrderItem(UpdateView):
    model = models.Orderitem
    template_name = 'Update.html'
    form_class = forms.OrderItemForm
    success_url = '/core/OrderItem'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# VendorItem
class VendorItemsList(ListView):
    model = models.VendorItems
    context_object_name = 'vendorItems'
    template_name = 'VendorItems.html'


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
    template_name = 'Delete.html'
    success_url = '/core/vendorItems'


class UpdateVendorItem(UpdateView):
    model = models.VendorItems
    template_name = 'Update.html'
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
    template_name = 'Delete.html'
    success_url = '/core/vendor'


class UpdateVendor(UpdateView):
    model = models.Vendor
    template_name = 'Update.html'
    form_class = forms.VendorForm
    success_url = '/core/vendor'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


# Item
class ItemList(ListView):
    model = models.Item
    context_object_name = 'Items'
    template_name = 'ItemList.html'


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
    template_name = 'Delete.html'
    success_url = '/core/item'


class UpdateItem(UpdateView):
    model = models.Item
    template_name = 'Update.html'
    form_class = forms.ItemForm
    success_url = '/core/item'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class HomePageView(TemplateView):
    template_name = "account/home.html"

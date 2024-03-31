from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'  # Update with your template name
    context_object_name = 'product'

# class ProductCreateView(CreateView):
#     model = Product
#     fields = ['name', 'description', 'price']  # Update with your fields
#     template_name = 'product_form.html'  # Update with your template name
#     success_url = reverse_lazy('product_list')  # Redirect to product list upon success

# class ProductUpdateView(UpdateView):
#     model = Product
#     fields = ['name', 'description', 'price']  # Update with your fields
#     template_name = 'product_form.html'  # Update with your template name
#     context_object_name = 'product'
#     success_url = reverse_lazy('product_list')  # Redirect to product list upon success

# class ProductDeleteView(DeleteView):
#     model = Product
#     template_name = 'product_confirm_delete.html'  # Update with your template name
#     success_url = reverse_lazy('product_list')  # Redirect to product list upon success

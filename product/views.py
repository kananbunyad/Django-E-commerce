
from msilib.schema import ListView
from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from product.models import Blog_Comment, Product,Blog
from product.forms import ProductReview,BlogForm
from core.forms import SubscriberForm
from django.http import HttpResponseForbidden

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from product.forms import ProductReviewForm,Blog_Comment
from core.forms import SubscriberForm
from django.views.generic import DetailView
from product.models import Categories, Product,ProductReview







class BlogView(ListView):
    template_name = 'blog.html'
    model = Blog

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_post'] = Blog.objects.all()
        
        return context





# def blog_detail(request):
#     comment_blog = Blog_Comment.objects.all() 
#     category = Product.objects.all() 

#     form = BlogForm()
#     form1 = SubscriberForm()
#     if request.method == 'POST':
#         form = BlogForm (data=request.POST)
#         form1 = SubscriberForm(data=request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy('blog_detail'))
#         elif form1.is_valid():
#             form1.save()
#             return redirect(reverse_lazy('blog_detail'))
#     context = {
#         'form' : form,
#         'form1' : form1,
#         'comment_blog': comment_blog,
#         'category':category
#     }
#     return render(request,'blog_detail.html',context)   

# def blog(request):
#     blog_post = Blog.objects.all() 
#     form = SubscriberForm()
#     if request.method == 'POST':
#         form = SubscriberForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy('home'))
#     context = {
#         'form' : form,
#         'blog_post': blog_post
#     }
#     return render(request, 'blog.html',context)




class BlogDetailView(FormMixin, DetailView):

    model = Blog
    template_name = 'blog_detail.html'
    form_class = BlogForm
    context_object_name = "blog_post"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_blog'] = Blog_Comment.objects.all()
        context['category'] = Product.objects.all() 
        context['popular_blogs'] = Blog.objects.all().exclude(id=self.object.id)

        return context

    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    
    def get_success_url(self):
        return "/blog"



def product_detail(request, pk):
    products = Product.objects.filter(id=pk)
    all_products = Product.objects.all()
    reviews = ProductReview.objects.filter(product=products[0].id)
    related_products = Product.objects.filter(category=products[0].category)
    form1 = SubscriberForm(data=request.POST)
    print(request.POST)
    if request.method == 'POST':
        ProductReview.objects.create(
            product=products[0],
            price_rate=request.POST.get('price_rate'),
            value_rate=request.POST.get('value_rate'),
            quality_rate=request.POST.get('quality_rate'),
            nickname=request.POST.get('nickname'),
            summary=request.POST.get('summary'),
            review=request.POST.get('review'),)
            
        if form1.is_valid():
            form1.save()
            
    context = {
        'form1' : form1,
        'products' : products,
        'related_products' : related_products,
        'all_products' : all_products,
        'reviews' : reviews
    }
    return render(request,'product-detail.html',context )




# class ProductDetailView(DetailView):
#     model = Product
#     form_class = ProductReview
#     context_object_name = 'product'
#     template_name = 'product-detail.html'

#     def get_successs_url(self):
#         return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})


def product_list(request):
    form = SubscriberForm()
    products = Product.objects.filter()
    categories = Categories.objects.all()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form,
        'categories' : categories,
        'products' : products
    }
    return render(request, 'product-list.html',context)

def quick_view(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form
    }
    return render(request, 'quick_view.html',context)







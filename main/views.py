from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import MessageForm
from .models import TagCategory, Product, CustomerReview
from account.models import UserAccount


class MainPageView(View):

    def get(self, request):
        categories = TagCategory.objects.all()
        products = Product.objects.all()[:8]
        reviews = CustomerReview.objects.all()[:3]
        return render(request, 'index.html', locals())


@login_required
def review_create(request):
    categories = TagCategory.objects.all()
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(request, messages.INFO, 'Your review was send successfully!')
            return redirect('all_reviews')
    else:
        form = MessageForm()
    return render(request, 'add_review.html', locals())
    

class AllReview(View):
    
    def get(self, request):
        categories = TagCategory.objects.all()
        reviews = CustomerReview.objects.all()
        return render(request, 'all_reviews.html', locals())


class CategoryProducts(View):

    def get(self, request, slug):
        categories = TagCategory.objects.all()
        category = TagCategory.objects.get(slug__iexact=slug)
        cat_products = category.product_category.all()
        return render(request, 'products.html', locals())


class About(View):

    def get(self, request):
        categories = TagCategory.objects.all()
        return render(request, 'about.html', locals())




    
    






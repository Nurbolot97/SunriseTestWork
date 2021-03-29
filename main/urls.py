from django.urls import path

from .views import (MainPageView, review_create, 
                    AllReview, CategoryProducts,
                    About)




urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('add-review/', review_create, name='add_review'),
    path('all-reviews/', AllReview.as_view(), name='all_reviews'),
    path('about/', About.as_view(), name='about'),
    path('category-products/<str:slug>/', CategoryProducts.as_view(), name='category_products'),
    
]
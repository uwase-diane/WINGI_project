from unicodedata import name
from django.urls import path
from django.urls import URLPattern
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import(
    OrderSummary,
    )

urlpatterns = [
    path('', views.products, name = 'index'),
    path('add-product', views.create_product, name='add-product'),
    path('product/<id>', views.product_details, name='product'),
    path('search/', views.search_item, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<id>', views.update_view, name='edit'),
    path('delete/<id>',views.delete_view, name='delete'),
    path('accounts/profile/', views.my_profile, name="profile"),
    path('category/<category>',views.product_category,name = 'category'),
    path('add-to-cart/<id>', views.add_to_cart, name="add-to-cart"),
    path('order_summary/', OrderSummary.as_view(), name="order_summary"),
    path('remove-single-item/<id>', views.remove_single_item, name="remove-single-item"),
    path('remove-from-cart/<id>', views.remove_from_cart, name="remove-from-cart"),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
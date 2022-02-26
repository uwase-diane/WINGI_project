from unicodedata import name
from django.urls import path
from django.urls import URLPattern
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.products, name = 'index'),
    path('add-product', views.create_product, name='add-product'),
    path('product/<id>', views.product_details, name='product'),
    path('search/', views.search_item, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<id>', views.update_view, name='edit'),
    path('delete/<id>',views.delete_view, name='delete'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
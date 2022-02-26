from email import message
from unicodedata import category
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Item,Category
from django.contrib import messages
from .forms import ItemForm

 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create_product(request):
    context ={}
 
    form = ItemForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/") 

    context['form']= form
    return render(request, "create_product.html", context)  
    


def products(request):
    items = Item.objects.all()
    categories = Category.get_category()
    return render(request, 'index.html', {"items": items, 'categories':categories})

def product_details(request, id):
    product_item = Item.objects.filter(id=id)  
    return render(request, "product_details.html", {"product_item": product_item})    

def product_category(request, category):
    items = Item.filter_by_category(category)
    categories = Category.get_category()
    context = {
        'items':items,
        'categories':categories
    }
    return render(request, 'shop.html', context)


def search_item(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        search_item = Item.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, "search.html", {"message": message, "items": search_item})

    else:
        messages.info(request, "You haven't searched for any term")
        return render(request, 'search.html') 

def dashboard(request):
    items = Item.objects.all()
    categories = Category.get_category()
    return render(request, 'dashboard.html', {"items": items, 'categories':categories})
    
def update_view(request, id):

    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Item, id = id)
 
    # pass the object as instance in form
    form = ItemForm(request.POST or None,files=request.FILES,instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/dashboard")   
    context['form']= form
    return render(request, 'edit_product.html', context)    

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Item, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/dashboard")
 
    return render(request, "delete_view.html", context)    
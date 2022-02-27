from email import message
from unicodedata import category
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .models import Item,Category,Order,Orderitem,Profile
from django.contrib import messages
from .forms import ItemForm
from django.utils import timezone
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
 

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
    return render(request, 'category.html', context)

def search_item(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        search_item = Item.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, "search.html", {"message": message, "items": search_item})
    else:
        messages.info(request, "You haven't searched for any term")
        return render(request, 'search.html')

def dashboard(request):
    items = Item.objects.all()
    categories = Category.get_category()
    paginate_by = 1
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
class OrderSummary(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(ordered=False)
            context = {
                'object': order
            }
            return render(self.request, "order_summary.html", context)
        except ObjectDoesNotExist:
            messages.error(request, "You do not have an active order")
            return redirect("/")

def my_profile(request):
    current_user = request.user
    return render(request, 'profile.html')

def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_item, created = Orderitem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        # check if order item is in the order
        if order.items.filter(item_id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("order_summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item  was added to your cart.")
            return redirect("order_summary")

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
         user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item  was added to your cart.")
        return redirect("order_summary")

def remove_single_item(request, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in the order
        if order.items.filter(item_id=item.id).exists():
            order_item = Orderitem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            # if quantity is  0
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()

            else:
                order.items.remove(order_item)

            messages.info(request, "This item  quantity was updated.")
            return redirect("order_summary")
        else:
            messages.info(request, "This item  was not in your cart.")
            return redirect("product", id=id)
    else:
        messages.info(request, "You don't have an active order")
        return redirect("product", id=id)

def remove_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )

    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in the order
        if order.items.filter(item_id=item.id).exists():
            order_item = Orderitem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item  was removed from your cart.")
            return redirect("order_summary")
        else:
            messages.info(request, "This item  was not in your cart.")
            return redirect("order_summary")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("order_summary") 
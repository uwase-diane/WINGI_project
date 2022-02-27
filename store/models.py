from itertools import product
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    profile_picture = models.ImageField(upload_to = 'profile_photos/', null=True)
    bio = models.CharField(max_length =300)

    @classmethod
    def get_profile(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name

    @classmethod
    def get_category(cls):
        categories = Category.objects.all()
        return categories

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'landing_images/')
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    #searching product 

    @classmethod
    def search_by_title(cls,search_term):
        certain_user = cls.objects.filter(title__icontains = search_term)
        return certain_user

    def __str__(self):
        return self.title

    @classmethod
    def filter_by_category(cls,category):
        product = Item.objects.filter(category__name=category).all()
        return product


class Orderitem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


    def get_total_item_price(self):
        return self.quantity * self.item.price    

    def get_final_price(self):
        return  self.get_total_item_price()

    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Orderitem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        total_discount = 0
        for order_item in self.items.all():
            total = total + order_item.get_final_price()
        
        return total

  
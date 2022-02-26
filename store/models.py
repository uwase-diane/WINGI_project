from itertools import product
from unicodedata import name
from django.db import models
from django.conf import settings

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
        certain_user = cls.objects.filter(category__icontains = search_term)
        return certain_user

    def __str__(self):
        return self.title

    # @classmethod
    # def filter_by_category(cls,category):
    #     product = Item.objects.filter(category__name=category).all()
    #     return product



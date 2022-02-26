from django import forms
from .models import Item
 
 
# creating a form
class ItemForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Item
 
        # specify fields to be used
        fields = ["title", "description","image","price","category"]


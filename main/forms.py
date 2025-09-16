from django.forms import ModelForm
from main.models import Items

class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ["name", "description", "category", "thumbnail", "is_featured", "price", "stock", "rating", "brand"]
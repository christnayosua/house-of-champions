from django.forms import ModelForm
from main.models import Products

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "description", "category", "thumbnail1", "thumbnail2", "thumbnail3", "is_featured", "price", "stock", "rating", "brand"]
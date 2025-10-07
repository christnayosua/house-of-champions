from django.forms import ModelForm
from main.models import Products

# Tambahan import untuk melindungi aplikasi web dari XSS
from django.utils.html import strip_tags

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "description", "category", "thumbnail1", "thumbnail2", "thumbnail3", "is_featured", "price", "stock", "rating", "brand"]


    # tambahan method untuk clean title and content saat handle AJAX request dan DOMpurify
    def clean_title(self):
        title = self.cleaned_data["title"]
        return strip_tags(title)

    def clean_content(self):
        content = self.cleaned_data["description"]
        return strip_tags(content)
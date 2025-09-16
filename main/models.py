import uuid
from django.db import models

# Create your models here.
class Items(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
        ('training', 'Training'),
        ('special', 'Special'),
        ('national', 'National'),
        ('classic', 'Classic'),
        ('derby', 'Derby')
    ]
    
    # Item wajib
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)
    
    # Attribute tambahan (opsional) -> butuh untuk informasi deskripsi item lebih lanjut
    # Selain itu, rating berguna agar dapat menampilkan barang-barang yang direkomendasikan oleh aplikasi berdasarkan review user lain
    stock = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    brand = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Penambahan attribute visitors untuk memberikan informasi popularitas item yang sering dilihat user
    visitors = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def is_items_hot(self):
        return self.visitors > 20
        
    def increment_views(self):
        self.visitors += 1
        self.save()
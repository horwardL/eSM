from django.db import models
from django.urls import reverse


class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Base):
    Category_Status = [(0, "Active"), (1, "InActive")]

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text="Unique category page URL.")
    description = models.TextField()
    meta_description = models.CharField("Meta Description", max_length=500, help_text="Content for description meta tag")
    meta_keywords = models.CharField("Meta Keywords", max_length=500, help_text="Comma separated set to SEO keywords for meta tag")
    category_status = models.IntegerField(choices=Category_Status, default=0)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_date']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalogueApp:catalogue", args=[self.slug])


class Market(Base):
    Market_Status = [(0, "Active"), (1, "InActive")]

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text="Unique market page URL.")
    description = models.TextField()
    meta_description = models.CharField("Meta Description", max_length=500, help_text="Content for description meta tag")
    meta_keywords = models.CharField("Meta Keywords", max_length=500, help_text="Comma separated set to SEO keywords for meta tag")
    market_status = models.IntegerField(choices=Market_Status, default=0)

    class Meta:
        db_table = 'markets'
        ordering = ['-created_date']
        verbose_name_plural = 'Markets'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalogueApp:market", args=[self.slug])
    


class Product(Base):
    Product_Status = [(0, "Active"), (1, "InActive")]

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text="Unique product page URL.")
    description = models.TextField()
    meta_description = models.CharField("Meta Description", max_length=500, help_text="Content for description meta tag")
    meta_keywords = models.CharField("Meta Keywords", max_length=500, help_text="Comma separated set to SEO keywords for meta tag")
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.BooleanField(default=True) #True = each, False = gram
    weigth = models.DecimalField(max_digits=15, decimal_places=2, blank=False, default=0.00)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0.00)
    image_url = models.CharField(max_length=500)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    markets = models.ManyToManyField(Market)
    product_status = models.IntegerField(choices=Product_Status, default=0)

    class Meta:
        db_table = 'products'
        ordering = ['-created_date']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalogueApp:product", args=[self.slug])

    def sale_price(self):
        return self.price if self.old_price > self.price else None
    

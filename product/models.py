from django.db import models
from django.forms import  DecimalField




class Blog(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50)
    username =  models.CharField(max_length=50)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    description =  models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.username



class Categories(models.Model):
    title = models.CharField(max_length=50)
    parent_category = models.ForeignKey("Categories", on_delete=models.CASCADE, null=True, blank=True)  



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    field_name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    code = models.IntegerField
    field_name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)
    discount = models.ForeignKey("Discount", on_delete=models.CASCADE,null=True, blank=True)
    category = models.ForeignKey("Categories",related_name='products', on_delete=models.CASCADE) 
    brand = models.ForeignKey("ProductBrand", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductBrand(models.Model):
    title = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Brand"
        verbose_name_plural = "Product Brands"


class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    product = models.ForeignKey("Product", related_name='review' ,on_delete=models.CASCADE)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Discount(models.Model):
    value = models.IntegerField(null=True, blank=True, default=0)
    is_percentage = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


  


class Propertie(models.Model):
    title =  models.CharField(max_length=50)
    category = models.ForeignKey("Categories", on_delete=models.CASCADE) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

class PropertieValue(models.Model):
    title =  models.CharField(max_length=50)
    category = models.ForeignKey("Propertie", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Property Value"
        verbose_name_plural = "Property Values"

    def __str__(self):
        return self.title

class ProductPropertieValue(models.Model):
    title =  models.CharField(max_length=50)
    property = models.ForeignKey("Product", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Property Value"
        verbose_name_plural = "Product Property Values"

    



class ProductReview(models.Model):

    product         = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, blank=True, related_name="product_reviews")

    RATES =[
        (1, "20"),
        (2, "40"),
        (3, "60"),
        (4, "80"),
        (5, "100"),
    ]


    value_rate      = models.IntegerField(choices=RATES)
    quality_rate    = models.IntegerField(choices=RATES)
    price_rate      = models.IntegerField(choices=RATES)
    nickname        = models.CharField(max_length=50)
    summary         = models.CharField(max_length=100)
    review          = models.CharField(max_length=500)
    

    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self) -> str:
        return self.summary


    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"


class Blog_Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=55)
    comment = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog Comment"
        verbose_name_plural = "Blog Comments"
    
    def __str__(self):
        return self.name



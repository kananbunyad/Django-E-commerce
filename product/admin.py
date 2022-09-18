from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import Categories,Product,Discount,Propertie,PropertieValue,Blog,ProductPropertieValue,ProductBrand,Review,ProductReview,Blog_Comment,Blog

admin.site.register([Discount,Propertie,PropertieValue,ProductPropertieValue,ProductBrand,Review,Blog])



class CategoriesAdmin(TranslationAdmin):
    pass

admin.site.register(Categories, CategoriesAdmin)


class ProductAdmin(TranslationAdmin):
    pass

admin.site.register(Product, ProductAdmin)


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'price_rate', 'value_rate', 'quality_rate', 'nickname', 'summary', 'review')
    list_filter = ('product', 'price_rate', 'value_rate', 'quality_rate', 'nickname', 'summary', 'review')
    search_fields = ('product', 'price_rate', 'value_rate', 'quality_rate', 'nickname', 'summary', 'review')
    list_per_page = 20

@admin.register(Blog_Comment)
class Blog_CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment')
    list_filter = ('name', 'email', 'comment')
    search_fields = ('name', 'email', 'comment')
    list_per_page = 20


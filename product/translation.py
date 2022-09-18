from modeltranslation.translator import translator, TranslationOptions
from product.models import Categories,Product



class CategoriesTranslationOptions(TranslationOptions):
    fields = ('title',)

class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Categories, CategoriesTranslationOptions)
translator.register(Product, ProductTranslationOptions)


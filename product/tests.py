from django.test import TestCase
from product.models import Categories,Discount,Product,Propertie    


class TestDiscountModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'is_percentage' : True,
        }
        cls.discount = Discount.objects.create(**cls.data1)
    
    def test_created_data(self):
        discount = Discount.objects.first()
        self.assertEqual(discount.is_percentage, self.data1['is_percentage'])

    @classmethod
    def tearDownClass(cls):
        Discount.objects.first().delete()
        del cls.discount
        del cls.data1


class TestCategoriesModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'title' : 'Shoes',
        }
        cls.categories = Categories.objects.create(**cls.data1)
    
    def test_created_data(self):
        categories = Categories.objects.first()
        self.assertEqual(categories.title, self.data1['title'])

    def test_str_method(self):
        self.assertEqual(str(self.categories), self.data1['title'])

    @classmethod
    def tearDownClass(cls):
        Categories.objects.first().delete()
        del cls.categories
        del cls.data1

class TestPropertieModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'title' : 'Shoes',
        }
        cls.categories = Categories.objects.create(**cls.data1)


        cls.data2 = {
            'title' : 'Color',
            'category' : cls.categories,
        }
        cls.propertie = Propertie.objects.create(**cls.data2)

    
    def test_created_data(self):
        propertie = Propertie.objects.first()
        self.assertEqual(str(propertie.category), self.data1['title'])

    @classmethod
    def tearDownClass(cls):
        Propertie.objects.first().delete()
        del cls.categories
        del cls.propertie
        del cls.data1
        del cls.data2


class TestPropertieValueModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'title' : 'Shoes',
        }
        cls.categories = Categories.objects.create(**cls.data1)

        cls.data2 = {
            'title' : 'Color',
            'category' : cls.categories,
        }
        cls.propertie = Propertie.objects.create(**cls.data2)


       
      

    
    

    @classmethod
    def tearDownClass(cls):
     
        del cls.categories
        del cls.propertie
  
        del cls.data1
        del cls.data2
    


class TestProductModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'title' : 'Shoes',
        }
        cls.categories = Categories.objects.create(**cls.data1)

        cls.data2 = {
            'title' : 'Color',
            'category' : cls.categories,
        }
        cls.propertie = Propertie.objects.create(**cls.data2)



        cls.data4 = {
            'is_percentage' : 'True',
        }
        cls.discount = Discount.objects.create(**cls.data4)

        cls.data5 = {
            'title' : 'Gros',
            'price' : 20,
            'discount' : cls.discount,
      
        }
        cls.product = Product.objects.create(**cls.data5)

    

    @classmethod
    def tearDownClass(cls):
        Product.objects.first().delete()
        del cls.categories
        del cls.propertie
        del cls.discount
        del cls.product
        del cls.data1
        del cls.data2

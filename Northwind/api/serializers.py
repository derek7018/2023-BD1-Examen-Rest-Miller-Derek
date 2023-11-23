from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class EmployeesSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class ShippersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippers
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    reportsto = EmployeesSerializer2(many=False)
    class Meta:
        model = Employees
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    customerid = CustomersSerializer(many=False)
    employeeid = EmployeesSerializer(many=False)
    shipvia = ShippersSerializer(many=False)

    class Meta:
        model = Orders
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    supplierid = SuppliersSerializer(many=False)
    categoryid = CategoriesSerializer(many=False)
    class Meta:
        model = Products
        fields = '__all__'

class OrderdetailsSerializer(serializers.ModelSerializer):
    productid = ProductsSerializer(many=False)
    class Meta:
        model = Orderdetails
        fields = '__all__'

class Punto1Serializer(serializers.ModelSerializer):
    productid = ProductsSerializer(many=False)
    categoryid = CategoriesSerializer(many=False)
    class Meta:
        model = Products
        fields = ['products_id','category_id']
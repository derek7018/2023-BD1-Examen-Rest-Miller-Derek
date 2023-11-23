from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from api.serializers import *
from api.models import *
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET', 'POST'])
def customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def customers_id(request, pk):
    try:
        customers = Customers.objects.get(cod_customer=pk)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = CustomersSerializer(customers, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomersSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customers.delete()
        return Response(status=status.HTTP_200_OK)


#------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def suppliers(request):
    if request.method == 'GET':
        suppliers = Suppliers.objects.all()
        serializer = SuppliersSerializer(suppliers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuppliersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def suppliers_id(request, pk):
    try:
        suppliers = Suppliers.objects.get(cod_suppliers=pk)
    except Suppliers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = SuppliersSerializer(suppliers, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuppliersSerializer(suppliers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        suppliers.delete()
        return Response(status=status.HTTP_200_OK)


#------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        categories= Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def categories_id(request, pk):
    try:
        categorie = Categories.objects.get(cod_categorie=pk)
    except Categories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = CategoriesSerializer(categories, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriesSerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=status.HTTP_200_OK)

#-------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def products_id(request, pk):
    try:
        product = Products.objects.get(cod_product=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = ProductsSerializer(products, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Products.delete()
        return Response(status=status.HTTP_200_OK)

#------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def orders(request):
    if request.method == 'GET':
        orders= Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def orders_id(request, pk):
    try:
        order = Orders.objects.get(cod_order=pk)
    except Orders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = OrdersSerializer(orders, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrdersSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Orders.delete()
        return Response(status=status.HTTP_200_OK)

#---------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def ordersdetails(request):
    if request.method == 'GET':
        ordersdetails = Orderdetails.objects.all()
        serializer = OrderdetailsSerializer(ordersdetails, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderdetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def orderdetails_id(request, pk):
    try:
        ordersdetail = Orderdetails.objects.get(cod_ordersdetail=pk)
    except Orderdetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = OrderdetailsSerializer(ordersdetails, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderdetailsSerializer(ordersdetails, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Orderdetails.delete()
        return Response(status=status.HTTP_200_OK)

#------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def employees(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employees_id(request, pk):
    try:
        employee = Employees.objects.get(cod_employee=pk)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET': 
        serializer = EmployeesSerializer(employees, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeesSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Employees.delete()
        return Response(status=status.HTTP_200_OK)
    


@api_view(['GET'])
def fechaMayor(request):
    orders = Orders.objects.filter(orderdate__gt="")
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fechaMenor(request):
    orders = Orders.objects.filter(orderdate__lt="")
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fechaRango(request):
    orders = Orders.objects.filter(orderdate__range=("",""))
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def empiezaCon(request):

    comienzacon = request.GET.get("comienzacon")
    if comienzacon:
        models.objects.filter(nombre__startwith=comienzacon)
    
    customers = Customers.objects.filter(contactname__startswith="A")
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def terminaCon(request):
    customers = Customers.objects.filter(contactname__endswith="a")
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ordenado(request):
    customers = Customers.objects.all().order_by('companyname')
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ordenadoAlReves(request):
    customers = Customers.objects.all().order_by('-companyname')
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

#Prueba
@api_view(['GET'])
def punto1(request):
    ventas = request.query_params.get('suppliers')
    categories_id = request.query_params.get('categories_id')
    
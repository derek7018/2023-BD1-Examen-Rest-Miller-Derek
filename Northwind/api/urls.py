
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('customers/', views.customers),
    path('customers/<str:customerid>/', views.customers),
    path('suppliers/', views.suppliers),
    path('suppliers/<int:supplierid>/', views.suppliers),
    path('categories/', views.categories),
    path('categories/<int:categoryid>/', views.categories),
    path('products/', views.products),
    path('products/<int:productid>/', views.products),
    path('orders/', views.orders),
    path('orders/<int:orderid>/', views.orders),
    path('orderDetails/', views.Orderdetails),
    path('orderDetails/<int:orderid>/', views.Orderdetails),
    path('employees/', views.employees),
    path('employees/<int:employeeid>/', views.employees),

    #filtros
    path('empiezacon/', views.empiezaCon),
    path('terminacon/', views.terminaCon),
    path('ordenado/', views.ordenado),
    path('ordenadoalreves/', views.ordenadoAlReves),
    path('fechamayor/', views.fechaMayor),
    path('fechamenor/', views.fechaMenor),

    #Prueba
    path('products/<int:productid>/<int:categoryid>/<int:ventasmin>/', views.punto1)

]

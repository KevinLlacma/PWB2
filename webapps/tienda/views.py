from django.shortcuts import render,redirect
from .models.customer import Customer
from .models.order import Order
from .models.product import Product
from .forms import CustomerForm,OrderForm,ProductForm
# Create your views here.


def index(request):
    customers=Customer.objects.all()
    productos=Product.objects.all()
    ordenes=Order.objects.all()
    data = {
        'customers': customers,
        'productos': productos,
        'ordenes': ordenes
    }
    return render(request,'index.html',data)
    


def crearCustomer(request):
    
    if request.method == 'GET':
        form = CustomerForm()
        return render(request,'crearCustomer.html', {'form': form})
    
    
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page or the index page



def crearProducto(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request,'crearProducto.html', {'form': form})
    
    
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page or the index page


def crearOrden(request):
    if request.method == 'GET':
        form = OrderForm()
        return render(request,'crearOrden.html', {'form': form})
    
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page or the index page
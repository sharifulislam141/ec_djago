from django.shortcuts import render 
from django.views import View
from .models import Product, Customer
from  .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'app/index.html')

class CategoryView(View):
    def get(self,request,val):
        products = Product.objects.filter(category = val)
        title = Product.objects.filter(category = val).values('title')
        return render(request, 'app/category.html',locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product= Product.objects.filter(title= val)
        title = Product.objects.filter(category = product[0].category).values('title')
        return render(request, 'app/category.html',locals())
    

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk = pk)
        return render(request,'app/productdetail.html',locals() )
   

def about(request):
    return render ( request,'app/about.html')
def contact (request):
    return render(request, 'app/contact.html')


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request,"Congration User Register Successful")
            print(form)
        else:
   
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/customerregistration.html',locals())
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        active_tab = 'profile'
        return render(request, 'app/profile.html', {'form': form, 'active_tab': active_tab})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        active_tab = 'profile'
        if form.is_valid():
            # Your form processing logic
            messages.success(request, "Profile saved successfully")
        else:
            messages.warning(request, "Invalid input")
        return render(request, 'app/profile.html', {'form': form, 'active_tab': active_tab})
def Address(request):
    add = Customer.objects.filter(user=request.user).first()
    print(add)  # Add this line to check the content of add
    active_tab = 'address'
    return render(request, 'app/address.html', {'add': add, 'active_tab': active_tab})

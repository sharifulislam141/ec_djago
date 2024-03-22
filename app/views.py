from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.views import View
from .models import Product, Customer
from  .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    products = Product.objects.all()
    customer = Customer.objects.filter(user = request.user).first()
    customer_name = customer.name if customer else None

    return render(request,'app/index.html', {'customer_name': customer_name})

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
    add = Customer.objects.filter(user=request.user)
    print(add)  # Add this line to check the content of add
    active_tab = 'address'
    return render(request, 'app/address.html', {'add': add, 'active_tab': active_tab})

 
class UpdateAddress(View):
    def get(self, request, pk):
        address = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=address)
        return render(request, 'app/updateAddress.html', {'form': form})
    
    def post(self, request, pk):
        address = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, "Address updated successfully")
            return redirect('app:address')  # Redirect to address page after successful update
        else:
            messages.error(request, "Invalid form data. Please correct errors.")
            return render(request, 'app/updateAddress.html', {'form': form})
        
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('app:change_password')
    template_name = 'app/change_password.html'

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed successfully.')
        return super().form_valid(form)
    
 

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

class PrintPasswordResetLinkView(PasswordResetConfirmView):
    def form_valid(self, form):
        print("form_valid method is called.")
        uidb64 = self.kwargs['uidb64']
        token = self.kwargs['token']
        UserModel = get_user_model()
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist) as e:
            print(f"Error: {e}")
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            reset_link = self.request.build_absolute_uri()
            print("Password reset link:")
            print(reset_link)
            # Pass reset_link to the context
            return render(self.request, 'app/password_reset_email.html', {'password_reset_link': reset_link})
        else:
            print("Invalid password reset link.")
        return super().form_valid(form)

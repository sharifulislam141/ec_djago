from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm
app_name = 'app'
urlpatterns = [
    path('',views.index, name = "Home"),
    path('about', views.about, name ="about"),
    path('contact', views.contact, name ="about"),
    path('category/<slug:val>', views.CategoryView.as_view(), name = "Category"),                               
    path('category-title/<val>', views.CategoryTitle.as_view(), name = "category-title"),                               
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name = "product-detail"),
    path('registration/',views.CustomerRegistrationView.as_view(), name= "registration"),
    path('accounts/login', auth_view.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm) ,name ='login')
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
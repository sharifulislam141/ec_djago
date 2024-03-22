from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

app_name = 'app'

urlpatterns = [
    # Your other URL patterns
    path('', views.index, name="Home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('category/<slug:val>/', views.CategoryView.as_view(), name="Category"),
    path('category-title/<val>/', views.CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name="product-detail"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.Address, name='address'),
    path('update_address/<int:pk>/', views.UpdateAddress.as_view(), name="UpdateAddress"),
    path('registration/', views.CustomerRegistrationView.as_view(), name="registration"),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('logout/', auth_views.LogoutView.as_view(next_page='app:login'), name='logout'),
    
    # Authentication-related URL patterns
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Your static and media URL patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

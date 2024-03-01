from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'app'
urlpatterns = [
    path('',views.index, name = "Home"),
    path('category/<slug:val>', views.CategoryView.as_view(), name = "Category"),                               
    path('category-title/<val>', views.CategoryTitle.as_view(), name = "category-title"),                               
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name = "product-detail")
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
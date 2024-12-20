from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from flowers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flowers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('', views.flower_list, name='flower_list'),
    path('flower/<int:flower_id>/', views.flower_detail, name='flower_detail'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:flower_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
"""
URL configuration for RSMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Accounts import views as acc_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', acc_views.dashboard, name='dashboard'),
    path('customer/<str:pk>/', acc_views.customer, name='customer'),
    path('inventory/', acc_views.inventory, name='inventory'),
    path('register/', acc_views.registration, name='register'),
    path('login/', acc_views.Login, name='login'),
    path('logout/', acc_views.LogoutPage, name='logout'),
    path('base/', acc_views.base, name='base'),
    path('index/', acc_views.index, name='index'),
    path('dash/', acc_views.dash, name='dash'),
    path('user/', acc_views.UserPage, name='user'),
    path('engineer/', acc_views.engineer, name='engineer'),
    
    path('workorder/', acc_views.workorder, name='workorder'),
    path('inventoryadj/', acc_views.InventoryAdjustment, name='inventoryadj'),
    path('allcustomers/', acc_views.allCustomers, name='allcustomers'),
    path('createorder/<str:pk>/', acc_views.createorder, name='createorder'),
    path('createorder/', acc_views.createorder2, name='createorder2'),
    path('order_form/', acc_views.createOrder, name='orderform'),
    path('update_form/<str:pk>/', acc_views.updateOrder, name='updateorder'),
    path('delete/<str:pk>/', acc_views.delete, name='delete'),

]
# <str:pk_test>/

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
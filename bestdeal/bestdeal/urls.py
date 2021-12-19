"""bestdeal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url
from request_quote import views 

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'items', views.RequirementDoc_Item)
router.register(r'req-doc', views.RequirementsDocView)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="BestDeal",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.bestdeal.com/policies/terms/",
      contact=openapi.Contact(email="contact@bestdeal.local"),
      license=openapi.License(name="BestDeal License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url('', include(router.urls)),
    path('req-doc/<int:pk>/items/', views.ItemsAPI.as_view()),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('',include('accounts.urls')),
]

"""PROJECT URL Configuration

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
from django.urls import path ,include
from saving.views import * # تم استيراد كل الفانكشن/الوظائف من التطبيق المطلوب
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/'    , admin.site.urls),# Go To The urs.py File In This app
    path('saving/'          , include('saving.urls')),# Go To The urs.py File In This app
    # path('accounts/', include('accounts.urls')),# Go To the urs.py file In This app
    
    ] 
urlpatterns += [
    path(''          , IndexHomeTemplateView.as_view(), name='IndexHomeTemplateView-URL'),
    path('about/'    , AboutTemplateView.as_view(), name='AboutTemplateView-URL'),
    ] 
    #Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
urlpatterns += [
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)




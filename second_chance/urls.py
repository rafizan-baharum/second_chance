"""second_chance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from second_chance.views import home_page

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('portfolio/', include(('portfolio.urls', 'portfolio'), namespace='portfolio')),
    path('academic/', include(('academic.urls', 'academic'), namespace='academic')),
    path('counseling/', include(('counseling.urls', 'counseling'), namespace='counseling')),
    path('financialaid/', include(('financialaid.urls', 'financialaid'), namespace='financialaid')),
    path('configuration/', include(('configuration.urls', 'configuration'), namespace='configuration')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
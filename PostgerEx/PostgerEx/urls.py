"""PostgerEx URL Configuration

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
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clg/', views.curd_op_c),
    path('dept/',views.departmentTable),
    path('lect/',views.lectTable),
    path('student/',views.studentTable),
    path('join/',views.joinTable),
    path('ljoin/',views.leftJTable),
    path('rjoin/',views.rightJTable),
    path('fjoin/',views.fullJTable),
    path('cross/',views.crossJTable)
]

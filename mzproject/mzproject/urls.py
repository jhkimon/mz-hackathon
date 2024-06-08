"""
URL configuration for mzproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),  # 메인배너 페이지
    path('input-name/', views.input_name, name='input_name'),  # 이름입력 페이지
    path('quiz/<int: id>', views.quiz_page, name='quiz_page'),  # 퀴즈 페이지
    path('result/', views.result_page, name='result_page'),  # 결과 확인 페이지
]
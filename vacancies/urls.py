"""vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app_vacancy.views import AllVacanciesView
from app_vacancy.views import CompaniesView
from app_vacancy.views import MainView
from app_vacancy.views import OneVacancyView
from app_vacancy.views import VacanciesSpecView

from app_vacancy.views import custom_handler404
from app_vacancy.views import custom_handler500

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies', AllVacanciesView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<str:specialty>/', VacanciesSpecView.as_view(), name='vacancies_by_specialty'),
    path('companies/<int:id>/', CompaniesView.as_view(), name='company'),
    path('vacancies/<int:id>/', OneVacancyView.as_view(), name='vacancy'),
    path('admin/', admin.site.urls),
]

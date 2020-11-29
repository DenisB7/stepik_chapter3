from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from app_vacancy.models import Company, Specialty, Vacancy


class MainView(View):

    def get(self, request):
        specialties = Specialty.objects.all()
        specialties_set = set()
        specialties_filter = []
        for spec_needed in specialties:
            for spec_lookup in specialties:
                if spec_needed.code not in specialties_set:
                    if spec_needed.code == spec_lookup.code:
                        specialties_set.add(spec_lookup.code)
                        code = spec_lookup.code
                        specialties_filter.append(Specialty.objects.filter(code=code))
                        break
        companies = Company.objects.all()
        companies_set = set()
        companies_filter = []
        for comp_needed in companies:
            for comp_lookup in companies:
                if comp_needed.name not in companies_set:
                    if comp_needed.name == comp_lookup.name:
                        companies_set.add(comp_lookup.name)
                        name = comp_lookup.name
                        companies_filter.append(Company.objects.filter(name=name))
                        break
        if not specialties_filter and not companies_filter:
            return HttpResponseNotFound('404 ошибка - ошибка на стороне '
                                        'сервера (страница не найдена)')
        main = {
            'specialties': specialties_filter,
            'companies': companies_filter,
        }
        return render(request, 'index.html', context=main)


class AllVacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.all()
        all_vancancies = {'vacancies': vacancies}
        return render(request, 'vacancies.html', context=all_vancancies)


class VacanciesSpecView(View):

    def get(self, request, specialty):
        vacs_of_spec = Specialty.objects.filter(code=specialty)
        if not vacs_of_spec:
            return HttpResponseNotFound('404 ошибка - ошибка на стороне '
                                        'сервера (страница не найдена)')
        vacancies_of_spec = {'vacs_of_spec': vacs_of_spec}
        return render(request, 'vacsspec.html', context=vacancies_of_spec)


class CompaniesView(View):

    def get(self, request, id):
        vacs_of_comps = Company.objects.filter(id=id)
        if not vacs_of_comps:
            return HttpResponseNotFound('404 ошибка - ошибка на стороне '
                                        'сервера (страница не найдена)')
        companies = {
            'vacs_of_comps': vacs_of_comps,
        }
        return render(request, 'company.html', context=companies)


class OneVacancyView(View):

    def get(self, request, id):
        vacancy = Specialty.objects.filter(id=id)
        if not vacancy:
            return HttpResponseNotFound('404 ошибка - ошибка на стороне '
                                        'сервера (страница не найдена)')
        vac = {'vacancy': vacancy}
        return render(request, 'vacancy.html', context=vac)


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 ошибка - ошибка на стороне '
                                'сервера (страница не найдена)')


def custom_handler500(request):
    return HttpResponseServerError('внутренняя ошибка сервера')

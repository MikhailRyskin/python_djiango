# from django.shortcuts import render
#
#
# def advertisement_list(request, *args, **kwargs):
#     advertisements = [
#         'Мастер на час',
#         'Выведение из запоя',
#         'Услуги экскаватора-погрузчика, гидромолота, ямобура'
#     ]
#     advertisements_1 = [
#         'Мастер на час',
#         'Выведение из запоя',
#         'Услуги экскаватора-погрузчика, гидромолота, ямобура'
#     ]
#     return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
#                                                                       'advertisements_1': advertisements_1})
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура',
        'Сбор урожая'
    ]


class Advertisements(View):

    get_count = 0
    post_count = 0

    def get(self, request):
        Advertisements.get_count += 1
        return render(request, 'advertisements/advertisement_list.html',
                      {'advertisements': advertisements, 'count': Advertisements.get_count})

    def post(self, request):
        Advertisements.post_count += 1
        return HttpResponse('предложение успешно создано')

from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Установить python. Был установлен.</li>'
                            '<li>Установить django. Установил.</li>'
                            '<li>Запустить сервер. Запустил.</li>'
                            '<li>Порадоваться результату. Ура!!!</li>'
                            '<li>5-ый элемент</li>'
                            '</ul>')

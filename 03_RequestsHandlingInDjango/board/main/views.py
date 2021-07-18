from django.shortcuts import render
from django.views import View

choices = [
        'выбор категории из списка,',
        'выбор региона из списка',
        ]


class Main(View):
    choices = [
        'выбор категории из списка,',
        'выбор региона из списка',
    ]

    def get(self, request):
        return render(request, 'main/main_list.html', {'choices': choices})

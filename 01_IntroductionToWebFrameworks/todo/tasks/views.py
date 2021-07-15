from django.http import HttpResponse
from django.views import View
import random

possible_tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Task 6', 'Task 7', 'Task 8', 'Task 9', 'Task 10']


def random_tasks():
    random_response = '<ul>'
    for task in random.sample(possible_tasks, 5):
        random_response += f'<li>{task}</li>'
    random_response += '</ul>'
    return random_response


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        response = random_tasks()
        return HttpResponse(response)

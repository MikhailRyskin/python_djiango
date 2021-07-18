import datetime
from django.http import HttpRequest


class LoggerUsersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # ip = request.META.get('REMOTE_ADDR')
        # server_name = request.META.get('SERVER_NAME')
        method = request.META.get('REQUEST_METHOD')
        host = HttpRequest.get_host(request)
        path = HttpRequest.get_full_path(request)
        now = datetime.datetime.now()
        with open('log_users.log', 'a', encoding='utf-8') as file:
            file.write(f'{now} {host}{path} {method} \n')

        response = self.get_response(request)
        return response

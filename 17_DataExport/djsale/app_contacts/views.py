from django.views.generic import TemplateView


class Contacts(TemplateView):
    template_name = 'app_contacts/contacts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = '"Рога и копыта"'
        context['address'] = 'C-Пб, Дворцовая пл., 1'
        context['phone'] = '+79217777777'
        context['email'] = 'roga@mail.ru'

        return context
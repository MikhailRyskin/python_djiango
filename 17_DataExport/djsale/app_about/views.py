from django.views.generic import TemplateView


class AboutList(TemplateView):
    template_name = 'app_about/about_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = '"Рога и копыта"'
        context['description'] = 'Операции с недвижимостью в вашем городе!'
        context['ownership_type'] ='ООО'
        return context
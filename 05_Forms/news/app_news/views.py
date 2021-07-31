from django.views.generic import ListView, CreateView, UpdateView
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import New, Comment
from .forms import CommentForm, CommentShortForm


class NewListView(ListView):
    model = New
    context_object_name = 'news'
    # queryset = Advertisement.objects.all()[:5]


class NewDetailView(View):
    def get(self, request, new_id):
        new = New.objects.get(id=new_id)
        comments = Comment.objects.all().filter(what_new=new_id)
        if request.user.is_authenticated:
            new_comment = CommentShortForm()
        else:
            new_comment = CommentForm()
        return render(request, 'app_news/new_detail.html', context={'new': new, 'comments': comments,
                                                                    'new_comment': new_comment, 'new_id': new_id})

    def post(self, request, new_id):
        new = New.objects.get(id=new_id)
        comments = Comment.objects.all().filter(what_new=new_id)
        if request.user.is_authenticated:
            new_comment = CommentShortForm(request.POST)
        else:
            new_comment = CommentForm(request.POST)
        if new_comment.is_valid():
            if request.user.is_authenticated:
                user = request.user
                user_name = request.user
            else:
                user = None
                user_name = f'{new_comment.cleaned_data["user_name"]} (аноним)'
            Comment.objects.create(what_new=new, user = user, user_name=user_name,
                                   text=new_comment.cleaned_data['text'])
            return HttpResponseRedirect('/news')
        return render(request, 'app_news/new_detail.html', context={'new': new, 'comments': comments,
                                                                    'new_comment': new_comment, 'new_id': new_id})


class NewFormView(CreateView):
    model = New
    fields = '__all__'
    success_url = '/news'


class NewEditFormView(UpdateView):
    model = New
    fields = '__all__'
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'new_id'
    success_url = '/news'

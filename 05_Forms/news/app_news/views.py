from django.views import generic
from .models import New, Comment
from .forms import NewForm, CommentForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View


class NewListView(generic.ListView):
    model = New
    # template_name = 'new_list.html'
    context_object_name = 'news'
    # queryset = Advertisement.objects.all()[:5]


class NewDetailView(View):
    def get(self, request, new_id):
        new = New.objects.get(id=new_id)
        comments = Comment.objects.all().filter(what_new=new_id)
        new_comment = CommentForm()
        return render(request, 'app_news/new_detail.html', context={'new': new, 'comments': comments,
                                                                    'new_comment': new_comment, 'new_id': new_id})

    def post(self, request, new_id):
        new = New.objects.get(id=new_id)
        comments = Comment.objects.all().filter(what_new=new_id)
        new_comment = CommentForm(request.POST)

        if new_comment.is_valid():
            Comment.objects.create(what_new=new, user_name=new_comment.cleaned_data['user_name'],
                                   text=new_comment.cleaned_data['text'])
            return HttpResponseRedirect('/news')
        return render(request, 'app_news/new_detail.html', context={'new': new, 'comments': comments,
                                                                    'new_comment': new_comment, 'new_id': new_id})


class NewFormView(View):

    def get(self, request):
        new_form = NewForm()
        return render(request, 'app_news/create.html', context={'new_form': new_form})

    def post(self, request):
        new_form = NewForm(request.POST)

        if new_form.is_valid():
            New.objects.create(**new_form.cleaned_data)
            return HttpResponseRedirect('/news')
        return render(request, 'app_news/create.html', context={'new_form': new_form})


class NewEditFormView(View):

    def get(self, request, new_id):
        new = New.objects.get(id=new_id)
        new_form = NewForm(instance=new)
        return render(request, 'app_news/edit.html', context={'new_form': new_form,
                                                              'new_id': new_id})

    def post(self, request, new_id):
        new = New.objects.get(id=new_id)
        new_form = NewForm(request.POST, instance=new)

        if new_form.is_valid():
            new.save()
            return HttpResponseRedirect('/news')
        return render(request, 'app_news/edit.html', context={'new_form': new_form,
                                                              'new_id': new_id})

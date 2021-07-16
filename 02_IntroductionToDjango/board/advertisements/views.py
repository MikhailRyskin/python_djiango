from django.shortcuts import render


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_list.html', {})


def advertisement_detail_1(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_detail_1.html', {})


def advertisement_detail_2(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_detail_2.html', {})


def advertisement_detail_3(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_detail_3.html', {})


def advertisement_detail_4(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_detail_4.html', {})


def advertisement_detail_5(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_detail_5.html', {})

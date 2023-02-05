import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect, Http404, HttpResponsePermanentRedirect
from django.urls import reverse

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Url
from .serializers import UrlSerializer
from . import services
from .forms import UrlForm


def short_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['url']

            if Url.objects.filter(original_url=original_url).exists():
                short_url = services.get_short_url(original_url=original_url)
                return render(request, 
                    'link_page.html', {
                    "hash_url":short_url,
                    "message":"already has a short version"}
                    )

            services.create_url_object(original_url=original_url)
            short_url = services.get_short_url(original_url=original_url)
            return render(request, 'link_page.html', {
                "hash_url":short_url
                })
    else:
        form = UrlForm()

    return render(request, 'main_page.html', {
        'form': form
        })


def redirect_url(request, hash):
    url_object = Url.objects.get(hash=hash)
    original_url = url_object.original_url

    if 'http' in original_url:
        url_object.add_click()
        return redirect(original_url)
    elif 'http' not in original_url:
        url_object.add_click()
        return redirect("https://www."+original_url)
    raise Http404('Page does not exist')


def click_statistics(request):
    urls = Url.objects.all()
    return render(request, 'statistics.html', {'urls':urls})
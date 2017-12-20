# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django imports
from django.shortcuts import render
from django.http import HttpResponse

# My imports
from .models import Runner

# Create your views here.
def index(request):
    """
    Home page test
    """
    return render(request, 'running_site/index.html')

def runners(request):
    """
    Example of a page that would display all the runners in the database.
    """
    runners = Runner.objects.order_by('first_name')
    context = {'runners': runners}
    return render(request, 'running_site/runners.html', context)

def runner(request, runner_id):
    """
    Individual runner page.
    """
    runner = Runner.objects.get(id=runner_id)
    performances = runner.performance_set.all()
    context = {'runner': runner, 'performances': performances}
    return render(request, 'running_site/runner.html', context)

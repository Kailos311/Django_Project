from django.shortcuts import render
from .models import Member
from django.http import HttpResponse
from django.template import loader

def members(request):
    member_list = Member.objects.all().values()
    template = loader.get_template('first.html')
    context = {
        'member_list': member_list
    }
    return HttpResponse(template.render(context, request))


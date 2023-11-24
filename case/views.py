from django.shortcuts import render
from .models import *
import random

def open_case(request, case_id):
    case = Case.objects.get(pk=case_id)
    items = case.item_set.all()
    random_item = random.choice(items)

    return render(request, 'case/open_case.html', {'case': case, 'random_item': random_item})

def case(request):
    items = Case.objects.all()
    context = {'cases':items}
    return render(request, 'case/case.html',context)
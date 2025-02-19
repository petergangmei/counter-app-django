from django.shortcuts import render
from .models import Counter

def home(request):
    obj = Counter.objects.get(id=1)
    context = {
        'count': obj.count
    }
    return render(request, 'home.html', context)


def counter(request, type):
    print('-------')
    obj = Counter.objects.get(id=1)
    print('-------')
    obj = Counter.objects.get(id=1)

    
    print(obj, type)
    if type == 'increase':
        obj.count += 1
        obj.save()
    if type == 'decrease':
        obj.count -= 1
        obj.save()
    
    context = {
        'count': obj.count
    }
    return render(request, 'home.html#counter', context)
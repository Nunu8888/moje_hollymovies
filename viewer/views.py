from django.shortcuts import render

def hello(request):
    adjectives = ['nice', 'cruel', 'blue', 'beautiful']
    name = 'Petr'
    context = {'adjectives': adjectives, 'name': name}

    #context = {'adjectives': ['nice', 'cruel', 'blue', 'beautiful']}
    return render(request=request, template_name='hello.html', context=context)


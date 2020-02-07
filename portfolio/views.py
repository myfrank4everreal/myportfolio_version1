from django.shortcuts import render

def viewPortfolio(request):
    projects = {}
    
    context = {'projects':projects}
    return render(request, 'portfolio/listandtuple.html', context)

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def contact(request):
    return HttpResponse("this is my contact page")


def count(request):
    data = request.GET["fulltextarea"]
    worl_list = data.split()
    ll =len(worl_list)

    repeatword ={}
    for word in worl_list:
        if word in repeatword:
            repeatword[word] +=1
        else:
            repeatword[word] = 1
    return render(request, 'count.html', {'fulltext':data, 'words':ll, 'rep':repeatword.items()})
from django.shortcuts import render, get_object_or_404
from .models import Problem, CompanyTag, CategoryTag
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    problem_list = Problem.objects.order_by('num')
    context = {
        'problem_lists': problem_list,
    }
    return render(request, 'mainApp/index.html', context)

def form(request):
    return render(request, 'mainApp/addProblem.html')

def addProblem(request):
    idNum = request.POST['problem_id']
    title = request.POST['problem_title']
    p = Problem(num=idNum, title=title)
    p.save()


    q = Problem.objects.filter(num=idNum)[0]

    company = request.POST['company_name']
    comp = CompanyTag(company_text=company, num_id=q)
    comp.save()

    tag = request.POST['category_name']
    cate = CategoryTag(category_text=tag, num_id=q)
    cate.save()

    return HttpResponseRedirect("/mainApp")
# def addTag(request, problem_id):


from django.shortcuts import render
from .models import Category,Question,Result,Reference,Academic
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    return render(request, 'dashboard/home.html')

def index(request):
    return render(request, 'dashboard/index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'quizapp/register.html', {
                'message': 'Passwords must match.',
                
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'quizapp/register.html', {
                'message': 'Username already taken.',
               
            })
        login(request, user)
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'dashboard/register.html', {
           
        })


def login_view(request):
    if request.method == 'POST':

        # Attempt to sign user in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'quizapp/login.html', {
                'message': 'Invalid username and/or password.',
               
            })
    else:
        return render(request, 'dashboard/login.html',  {
          
        })


def logout_view(request):
    logout(request)
    #return HttpResponseRedirect(reverse('index'))
    return redirect('index')





#@login_required(login_url='/login')
def category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'dashboard/category.html', context)


@login_required(login_url='/')
def question(request, pk):
    if request.method == 'POST':
        gotMarks = 0
        attempted = 0
        correct = 0
        incorrect = 0
        totalNumberOfQuestions = 0
        totalMarks = 0
        questions = Question.objects.filter(categoryid=pk)
        category = Category.objects.filter(id=pk)
        name = ''
        for ca in category:
            name=ca.title
            totalNumberOfQuestions = 10
            totalMarks = 10
        for q in questions:
            print(request.POST.get(q.questionText))
            print(q.answer)
            print()
            if q.answer == request.POST.get(q.questionText):
                gotMarks = gotMarks+1
                attempted = attempted+1
                correct = correct+1
            elif q.answer != request.POST.get(q.questionText):
                attempted = attempted+1
                incorrect = incorrect+1

        result = Result(user=request.user,
                        category=name,
                        total_questions=totalNumberOfQuestions,
                        total_marks=totalMarks,
                        got_marks=gotMarks,
                        attempted=attempted,
                        correct=correct,
                        incorrect=incorrect)
        result.save()
        return redirect('result')

    else:
        category = Category.objects.filter(id=pk)
        questions = Question.objects.filter(categoryid=pk)
        context = {
            'category': questions,
            'questions':questions
            }
    return render(request, 'dashboard/question.html', context)

@login_required(login_url='/')
def result(request):
    results=Result.objects.filter(user=request.user).order_by('id').reverse().first()
    category=Category.objects.filter(title=results.category)
    context={
        'result':results,
        'category':category
    }
    return render(request,'dashboard/result.html',context)

def reference(request,pk):
    category=Category.objects.filter(title=pk).first()
    references=Reference.objects.filter(categoryid=category.id)
    questions=Question.objects.filter(categoryid=category.id)

    context={
        'references':references,
        'category':category,
        'questions':questions
    }
    return render(request,'dashboard/reference.html',context)

def academic(request):
    return render(request, 'dashboard/academic.html')




#@login_required(login_url='/login')
def academic(request):
    academics = Academic.objects.all()
    context = {
        'academics': academics
    }
    return render(request, 'dashboard/academic.html', context)


def subject(request, pk):
    subject = Academic.objects.get(pk=pk)
    return render(request, 'dashboard/subject.html', {'subject':subject})
        

# Create your views here.

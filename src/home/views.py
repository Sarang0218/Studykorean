from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# import redirects from django.shortcuts
from django.contrib.auth import authenticate, login
from .models import Question, Student
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
  return render(request, 'home.html')

@csrf_exempt
def signupview(request):
  if request.method == 'POST':
    # create a user
    user = User.objects.create_user(
      username=request.POST['username'],
      password=request.POST['password'],
    )
    user.save()
    login(request, user)
    Student.objects.create(user=user, idNum=request.POST["id"], diff=0)
    
    return redirect("tabs")
    
  return render(request, 'signup.html')

def maintab(request):
  return render(request, "tabs.html")



@csrf_exempt
def loginview(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        return redirect("tabs")
    return render(request, 'login.html')
  return render(request, 'login.html')

def quiz(request):
  user = request.user
  if user.is_authenticated:
    question = pickProblem(user)
    
    if question.qType == "OX":
      answer = question.Oxproblem.answer
      if answer:
        return render(request, 'ox.html', {"AnswerO":"/correct", "AnswerX":"/incorrect", "question":question.Oxproblem.question_text})
      else:
        return render(request, 'ox.html', {"AnswerO":"/incorrect", "AnswerX":"/correct", "question":question.Oxproblem.question_text})
    elif question.qType == "MC":
      answer = question.MultipleChoiceProblem.answer
    elif question.qType == "SA":
      answer = question.ShortAnswerProblem.answer
  else:
    return render(request, 'login.html')    

def pickProblem(user):
  stu = Student.objects.get(user=user)
  qs = Question.objects.filter(difficulty=stu.diff)
  for que in qs:
    if (stu not in que.solvedby.all()):
      return que
  raise Exception("에러 101 - 질문 없음")

  
def correct(request):
  
  stu = Student.objects.get(user=request.user)
  if stu.diff < 6:
    stu.diff += 1
    stu.save()
  return redirect("quiz")

def incorrect(request):
  stu = Student.objects.get(user=request.user)
  if stu.diff > 0:
    stu.diff -= 1
    stu.save()
  return redirect("quiz")
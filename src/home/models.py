from django.db import models
from django.contrib.auth.models import User
from quiz.models import OX, ShortAnswer, MultiChoice
# Create your models here.

class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  idNum = models.CharField(max_length=5)
  diff = models.IntegerField(default=0)
  
  def __str__(self):
    return f"학생: {self.user.username}, 학번: {self.idNum}"

  

class Question(models.Model):
  Q_TYPE = [
    ("OX", "OX문제"),
    ("SA", "Short Answer"),
    ("MC", "Multi Choice"),
  ]
  qType = models.CharField(max_length=2, choices=Q_TYPE, null=True)
  
  Oxproblem = models.ForeignKey(OX, on_delete=models.CASCADE, null=True, blank=True)
  ShortAnswerProblem = models.ForeignKey(ShortAnswer, on_delete=models.CASCADE, null=True, blank=True)
  MultiChoiceProblem = models.ForeignKey(MultiChoice, on_delete=models.CASCADE, null=True, blank=True)

  
  difficulty = models.IntegerField(default=0)
  correct_answers = models.IntegerField(default=0, null=True)
  
  trys = models.IntegerField(default=0, null=True)
  solvedby = models.ManyToManyField(User, related_name='solvedby', blank=True)
  
  def markAsCorrect(self, user):
    stu = Student.objects.get(user=user)
    self.correct_answers += 1
    self.trys += 1
    self.solvedby.append(user)
    stu.diff += 1
    
    stu.save()
    self.save()

  def markAsIncorrect(self, user):
    stu = Student.objects.get(user=user)
    stu.diff -= 1
    stu.save()

    
  def __str__(self):
    if self.qType == "SA":
      if (self.trys > 0):
        return f"질문: {self.ShortAnswerProblem.question_text}, 답: {self.ShortAnswerProblem.answer}, 난이도: {self.difficulty}, 정답 비율: {self.correct_answers/self.trys}"
      else:
        return f"질문: {self.ShortAnswerProblem.question_text}, 답: {self.ShortAnswerProblem.answer}, 난이도: {self.difficulty}"
    elif self.qType == "MC":
      if (self.trys > 0):
        return f"질문: {self.MultiChoiceProblem.question_text}, 답: {self.MultiChoiceProblem.answer}, 난이도: {self.difficulty}, 정답 비율: {self.correct_answers/self.trys}"
      else:
        return f"질문: {self.MultiChoiceProblem.question_text}, 답: {self.MultiChoiceProblem.answer}, 난이도: {self.difficulty}"
    elif self.qType == "OX":
      if (self.trys > 0):
        return f"질문: {self.Oxproblem.question_text}, 답: {self.Oxproblem.answer}, 난이도: {self.difficulty}, 정답 비율: {self.correct_answers/self.trys}"
      else:
        return f"질문: {self.Oxproblem.question_text}, 답: {self.Oxproblem.answer}, 난이도: {self.difficulty}"
    else:
      raise Exception("에러 100 문제 문자화 오류")
    



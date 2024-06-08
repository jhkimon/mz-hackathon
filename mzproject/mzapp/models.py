from django.db import models

class Question(models.Model):
    quiz = models.TextField()  # 문제의 텍스트
    answer = models.IntegerField()  # 정답 (보기의 인덱스)
    op1 = models.TextField()  # 보기 1
    op2 = models.TextField()  # 보기 2
    op3 = models.TextField()  # 보기 3
    op4 = models.TextField()  # 보기 4
    
    def __str__(self):
        return self.quiz

class User(models.Model):
    user_count = models.IntegerField(default=1)  # 사용자 수

    def __str__(self):
        return str(self.user_count)
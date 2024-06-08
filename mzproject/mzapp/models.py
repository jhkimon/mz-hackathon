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
    name = models.CharField(max_length=255)  # 사용자의 이름
    start_time = models.DateTimeField()  # 퀴즈 시작 시간
    total_count = models.IntegerField()  # 총 문제 개수
    correct_count = models.IntegerField()  # 맞춘 문제 개수
    end_time = models.DateTimeField()  # 퀴즈 종료 시간

    def __str__(self):
        return self.name


class Reward(models.Model):
    name = models.CharField(max_length=255)  # 보상 이름
    image = models.ImageField(upload_to='images/')  # 보상 이미지
    
    def __str__(self):
        return self.name

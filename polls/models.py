from django.db import models


# Create your models here. 모델만들기
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 데이터 타입 문자열
    pub_date = models.DateTimeField('date published')  # 데이터 타입 날짜


def __str__(self):
    return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 칼럼은 외래키로 Question과 연결됨
    choice_text = models.CharField(max_length=200)  # 문자열
    votes = models.IntegerField(default=0)  # 정수


def __str__(self):
    return self.choice_text

# 테이블 두개 만드는 것 부모테이블 자식테이블

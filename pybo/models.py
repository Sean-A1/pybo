from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    # some_user.author_question.all()
    
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)   
    # 질문이나 답변이 언제 수정되었는지
    # null=True는 데이터베이스에서 modify_date 칼럼에 null을 허용
    # blank=True는 form.is_valid()를 통한 입력 데이터 검증 시 값이 없어도 된다는 의미
    # null=True, blank=True는 어떤 조건으로든 값을 비워둘 수 있음을 의미
    
    voter = models.ManyToManyField(User, related_name='voter_question')
    
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # 질문이나 답변이 언제 수정되었는지
    voter = models.ManyToManyField(User, related_name='voter_answer')
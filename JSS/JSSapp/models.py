from django.db import models
from django.contrib.auth.models import User

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자 foreign키 설정 (작성자 회원탈퇴시 작성글 자동으로 삭제 -> cascade옵션)
    # 기존 데이터에는 author가 없으므로 migrations 거부됨 -> null=True 옵션을 주거나 default값을 주면 해결
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# hyosun / 1212

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE)

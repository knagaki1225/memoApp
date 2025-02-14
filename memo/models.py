from django.db import models
from django.contrib.auth.models import User #Userモデル
from django.urls import reverse # reverse関数

class Memo(models.Model):
    title = models.CharField(max_length=10, default="Untitled")
    content = models.TextField()
    tag = models.ForeignKey("Tag", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse("memo:index")
    
class Tag(models.Model):
    tagname = models.CharField(max_length=10)

    def __str__(self):
        return self.tagname
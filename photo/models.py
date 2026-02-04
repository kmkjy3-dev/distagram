from django.db import models
from django.conf import settings
# Create your models here.
from django.urls import reverse
class Photo(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photos/default.jpg')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.author.username} {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
    
    class Meta:
        ordering = ['-updated_at']

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

# 
class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ✅ 좋아요, 싫어요 필드 추가
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True)
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_comments', blank=True)

    def __str__(self):
        return f"{self.author.username} - {self.text[:20]}"
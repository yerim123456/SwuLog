from django.db import models

from accountapp.models import CustomUser


class Post(models.Model):
    ALIGNMENT_CHOICES = (
        ('left', 'Left Align'),
        ('center', 'Center Align'),
        ('right', 'Right Align'),
    )

    FONT_CHOICES = (
        ('system', '시스템 폰트'),
        ('nanum_gothic', '나눔고딕'),
        ('nanum_myungjo', '나눔명조'),
        ('barun_gothic', '바른고딕'),
    )
    title = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    alignment = models.CharField(max_length=10, choices=ALIGNMENT_CHOICES)
    font = models.CharField(max_length=20, choices=FONT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Photo(models.Model):
    post = models.ForeignKey(Post, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_photos')

    def __str__(self):
        return self.image.name

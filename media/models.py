from django.db import models

class Media(models.Model):
    IMAGE = 'img'
    VIDEO = 'vid'
    MEDIA_CHOICES = [
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    ]
    title = models.CharField(max_length=100)
    media_type = models.CharField(
        max_length=3,
        choices=MEDIA_CHOICES,
        default=IMAGE,
    )
    media_file = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"

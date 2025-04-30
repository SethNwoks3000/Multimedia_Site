from django.shortcuts import render
from .models import Post

def post_detail(request):
    post = Post.objects.first()
    return render(request, 'media/post_detail.html', {'post': post})

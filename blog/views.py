from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import ArtistInfo

def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	artists=ArtistInfo.objects.all()
	return render(request, 'blog/index.html', {'posts':posts, 'artists':artists})


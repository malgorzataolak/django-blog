from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .models import ArtistInfo
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
import blog.lastfm as lastfm


def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	artists=ArtistInfo.objects.all()
	lastfm.user="margo121"
	lastfm.period="12month"
	lastfm.limit="10"
	res=lastfm.get_top_artists()
	res2=lastfm.generate_albums()
	res3=lastfm.generate_tracks()
	return render(request, 'blog/index.html', {'posts':posts, 'artists':artists, 'res': res, 'res2' : res2, 'res3' :res3})


def post_detail(request, pk):
	post=get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method=="POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form=PostForm()
	return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
	post=get_object_or_404(Post, pk=pk)
	if request.method=="POST":
		form=PostForm(request.POST, instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form=PostForm(instance=post)
	return render(request, 'blog/post_new.html',{'form':form})


def add_comment(request, pk):
	post=get_object_or_404(Post, pk=pk)
	if request.method=="POST":
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.post=post
			comment.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form=CommentForm()
	return render(request, 'blog/add_comment.html', {'form':form})

@login_required
def comment_approve(request, pk):
	comment=get_object_or_404(Comment, pk=pk)
	comment.approve()
	return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
	comment=get_object_or_404(Comment,pk=pk)
	post_pk=comment.post.pk
	comment.delete()
	return redirect('blog.views.post_detail', pk=post_pk)


def your_rankings(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	artists=ArtistInfo.objects.all()
	lastfm.user="margo121"
	lastfm.period="12month"
	lastfm.limit="10"
	res=lastfm.get_top_artists()
	res2=lastfm.generate_albums()
	res3=lastfm.generate_tracks()

	if request.method=="POST":
		lastfm.user=request.POST['search_user']
		if lastfm.is_user():
			new_period=request.POST['set_period']
			if new_period not in lastfm.periods:
				msg2="Został wpisany zły zakres, wypełnij jeszcze raz :)"
				return render(request,'blog/index.html', {'posts':posts, 'artists':artists, 'res': res, 'res2' : res2, 'res3' :res3, 'msg2':msg2});
			szukanedla=lastfm.user;
			lastfm.period=new_period
			lastfm.limit=request.POST['set_limit']
			r=lastfm.get_top_artists()
			r2=lastfm.generate_albums()
			r3=lastfm.generate_tracks()
			return render(request,'blog/index.html', {'posts':posts, 'artists':artists, 'res': res, 'res2' : res2, 'res3' :res3, 'szukanedla': szukanedla, 'r':r, 'r2':r2, 'r3':r3})
		else:
			msg="Taki użytkownik nie istnieje :("
			return render(request,'blog/index.html', {'posts':posts, 'artists':artists, 'res': res, 'res2' : res2, 'res3' :res3, 'msg':msg})

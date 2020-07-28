from django.shortcuts import render,get_object_or_404,redirect
from main.models import MovieInfo
from detailapp.models import Comment
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

def detail(req,movie_id):
    movie = get_object_or_404(MovieInfo,pk= movie_id)
    Comments = Comment.objects.filter(movie_id = movie.id)
    new = CommentForm()
    total = 0
    total_num =0
    for comment in Comments : 
        total += comment.grade 
        total_num += 1
    total /= total_num
    return render(req,'detail.html',{'movie' : movie,'Comments':Comments,'score':total,'form':new})

@login_required
def like(request, comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    comment.like.add(request.user)
    comment.save()    
    return redirect('/detail/' +str(comment.movie.id))

@login_required
def cancel(request, comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    comment.like.remove(request.user)
    comment.save()    
    return redirect('/detail/' +str(comment.movie.id))

def delete(req,comment_id):
    comments = get_object_or_404(Comment, pk = comment_id)
    comments.delete()
    return redirect('searchlist')


def new(request,movie_id):
    form = CommentForm(request.POST)
    movie = get_object_or_404(MovieInfo,pk=movie_id)
    if form.is_valid() :
        print(form)
        content = form.save(commit=False)
        content.movie = movie
        content.user = request.user
        content.save()
        return redirect(f"/detail/{content.movie.id}")
    else :
        return redirect('re')






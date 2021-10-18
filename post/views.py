from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment, like
from django.http import HttpResponse
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def post_list(request,category_slug=None):
    category= None
    category_list=Category.objects.all()
    post_list=Post.objects.all()
    post_list = post_list.filter(status = 'published')

    if category_slug:
        category = get_object_or_404(Category , slug=category_slug)
        post_list = post_list.filter(category=category)

    paginator = Paginator(post_list,8)
    current_page_number = request.GET.get('page')
    try :
        post_list = paginator.get_page(current_page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request,'post/list.html',{'post_list':post_list,
                                             'category':category,
                                             'category_list':category_list})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, created__year=year, created__month=month, created__day=day, slug=slug)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'your comment added')
    else:
        form = CommentForm()

    return render(request,'post/detail.html', {'post':post , 'comments':comments, 'form':form})


@login_required
def do_like(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	new_like = like(post=post, user=request.user)
	new_like.save()
	messages.success(request, 'your liked added', 'success')
	return redirect('post:post_detail', post.created.year, post.created.month, post.created.day, post.slug)

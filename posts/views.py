from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


from .forms import PostForm

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


from .models import Post

@login_required
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    disable_select1 = post.answered
    disable_select2 = post.answered
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer == 'select1_content':
            post.select1_users += 1
            post.select2_users = 0
        elif answer == 'select2_content':
            post.select2_users += 1
            post.select1_users = 0
        disable_select1 = True
        disable_select2 = True
        post.save()
        return redirect('posts:detail', post.pk)
    context ={
        'post': post,
        'disable_select1': disable_select1,
        'disable_select2': disable_select2,

    }
    return render(request, 'posts/detail.html', context)



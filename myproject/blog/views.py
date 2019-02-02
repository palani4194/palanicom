from django.shortcuts import render, get_object_or_404,redirect
from blog.models import Post
from django.utils import timezone
from .forms import PostForm,CommentForm
from .models import Post, Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from blog.forms import RegistrationForm,ProfileEditForm
from django.contrib.auth import update_session_auth_hash



# list view
@login_required
def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'post_view':posts})

# detail view
@login_required
def post_detail_view(request, pk):
    # import ipdb; ipdb.set_trace()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail_view.html', {'post': post})


# create view
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            form.save()
            return redirect('post_detail_view', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})


# edit view

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_view', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):

    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail_view', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')




@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail_view', pk=pk)





def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail_view', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})




@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail_view', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail_view', pk=comment.post.pk)


# about page
# def about(request):
#     return render(request, 'blog/about.html',)

# home page
def home(request):
    return render(request, 'blog/home.html',)

# logout page
def logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }

    return render(request, 'blog/login.html', context)



# register page
def register(request):

    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'registration/register.html',args)

# view profile page
@login_required
def profile(request):
        args = {'user':request.user}
        return render(request,'registration/profile.html',args)

# profile edit
@login_required
def profile_edit(request):

    if request.method =="POST":
        form = ProfileEditForm(request.POST,instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('/blog/profile/')
    else:
        form = ProfileEditForm(instance= request.user)
        args = {'form':form}
        return render(request,'registration/profile_edit.html',args)

# change_password page
def change_password(request):

    if request.method =="POST":
        form = PasswordChangeForm(data= request.POST,user= request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/blog/profile/')
        else:
            return redirect('blog/change-password/')
    else:
        form = PasswordChangeForm(user= request.user)
        args = {'form':form}
        return render(request,'registration/change_password.html',args)

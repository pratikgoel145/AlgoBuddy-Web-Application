from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post, Markread
from .forms import CommentForm

# def error(request):
#     return render(request, 'contents/error.html')

@login_required
def display(request):
   form = CommentForm(None)
   return render(request, 'contents/content.html', {'all_content': Post.objects.all(),
                                                    'selected_post': Post.objects.get(title="Bubble Sort"),
                                                    'form': form})
@login_required
def favorite(request, post_id):
    form = CommentForm(None)
    try:
        selected_post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, 'contents/error.html')
    return render(request, 'contents/content.html', {'all_content': Post.objects.all(),'selected_post': Post.objects.get(id=post_id),
                                                     'form': form})


@login_required
def markasread(request, post_id):
    try:
        selected_post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, 'contents/error.html')
    if request.user.is_authenticated():
        mark = False
        for temp in selected_post.markread.all():
            if temp.user == request.user.username:
                mark = True
                sample = Markread.objects.get(user=request.user.username, post = Post.objects.get(pk=post_id))
                sample.delete()
                return render(request, 'contents/content.html', {'all_content': Post.objects.all(),
                                                                 'selected_post': Post.objects.get(id=post_id),
                                                                 'status': 'NOT READ'})
        if not mark:
            Markread.objects.create(post=Post.objects.get(id=post_id), user=request.user.username)
    return render(request, 'contents/content.html',
                  {'all_content': Post.objects.all(), 'selected_post': Post.objects.get(id=post_id), 'status': 'READ'})


@login_required
def add_comment(request, post_id):
    template_name = 'contents/content.html'
    if request.method == 'POST':
        form = CommentForm(request.POST)
        try:
            selected_post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return render(request, 'contents/error.html')
        if form.is_valid() and request.user.is_authenticated():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(id=post_id)
            comment.user = request.user
            comment.save()
    return render(request, 'contents/content.html',
                      {'all_content': Post.objects.all(), 'selected_post': Post.objects.get(id=post_id),
                       'form': CommentForm(None)})


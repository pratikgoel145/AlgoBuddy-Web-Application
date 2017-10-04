from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from content.models import Post


@login_required
def index(request):
    return render(request, 'dashboard/details.html',{'all_content': Post.objects.all})

def error(request):
    return render(request, 'contents/error.html')
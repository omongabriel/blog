from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def post_list(request):
    posts_lists = Post.published.all()

    paginator = Paginator(posts_lists,2)
    page_number = request.GET.get('page',1)
    posts = paginator.get_page(page_number)
    print(posts.has_previous())
    

    return render(request,'blog/post/list.html',{'posts':posts})

def post_detail(request,yr,mn,dy,slug):
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,slug=slug,publish__year=yr,publish__month=mn,publish__day=dy)
  

    return render(request,'blog/post/detail.html',{'post':post})


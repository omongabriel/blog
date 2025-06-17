from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import EmailPostForm
from django.http import HttpResponse
from django.core.mail import send_mail


def post_share(request,id):
    post = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            message = (f"Read the title {post.title} at {post_url}\n\n"
                       f"{cd['name']}\'s Comment: {cd['comments']}")
            subject = (
                f"{cd['name']} ({cd['email']})"
                f"ecommends you read {post.title}"
            )
            
            send_mail(message=message,subject=subject,from_email=None,recipient_list=[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request,'blog/post/share.html',{'form':form,'post':post,'sent':sent})         



class PostListView(ListView):
    template_name = 'blog/post/list.html'
    context_object_name = 'posts'
    queryset = Post.published.all()
    paginate_by = 2

# Create your views here.
# def post_list(request):
#     posts_lists = Post.published.all()

#     paginator = Paginator(posts_lists,2)
#     page_number = request.GET.get('page',1)
#     posts = paginator.get_page(page_number)
#     print(posts.has_previous())
    

    # return render(request,'blog/post/list.html',{'posts':posts})

def post_detail(request,yr,mn,dy,slug):
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,slug=slug,publish__year=yr,publish__month=mn,publish__day=dy)
  

    return render(request,'blog/post/detail.html',{'post':post})


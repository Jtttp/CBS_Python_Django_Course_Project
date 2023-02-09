from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from .models import Post, Likes
from .forms import CommentsForm


class PostView(View):
    """This class publish posts"""

    # def get(self, request):
    #     posts = Post.objects.all()
    #     return render(request, 'blog/blog.html', {'post_list': posts})

    def get(self, request):
        posts = Post.objects.all()
        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/blog.html', {'post_list': posts, 'page_obj': page_obj, 'paginator': paginator})


class PostDetail(View):
    """Separate page for each posts"""

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})


class AddComments(View):
    """Add comments to the page"""

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    """Visitors can add likes"""

    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class DisLike(View):
    """Visitors can add dislikes"""

    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            dislike = Likes.objects.get(ip=ip_client)
            dislike.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')

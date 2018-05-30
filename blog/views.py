from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.



def post_list(request):
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts = Post.objects.order_by('published_date')
	test=123
	print(posts)
	return render(request, 'blog/post_list.html',{'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
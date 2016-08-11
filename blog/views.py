
from blog.models import BlogsPost
from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    print blog_list
    print len(blog_list)
    for blog in blog_list:
        print blog.body, blog.title, blog.timestamp
    return render_to_response('index.html', {'blog_list': blog_list})

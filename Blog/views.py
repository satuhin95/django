from django.shortcuts import render

# Create your views here.

def BlogList(request):
    return render(request, 'Blog/blog_list.html', context={})
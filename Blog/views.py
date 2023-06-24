from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView , DetailView, View, TemplateView, DeleteView
from Blog.models import Blog, Comment, Likes
from django.urls import reverse , reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from Blog.forms import CommentForm
# Create your views here.


class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'Blog/add_blog.html'
    fields = ('blog_title','blog_contain','blog_image')

    def form_valid(self, form):
        blogObj = form.save(commit=False)
        blogObj.author = self.request.user
        title = blogObj.blog_title
        blogObj.slug = title.replace(" ","-") + '-' + str(uuid.uuid4())
        blogObj.save()
        return HttpResponseRedirect(reverse('index'))
    
class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'Blog/blog_list.html'


@login_required
def blog_details(request, slug):

    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog, user=request.user)
    if already_liked:
        liked = True
    else:
        liked =False    

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.user = request.user
            comment.blog = blog
            comment.save()

            return HttpResponseRedirect(reverse('Blog:blog_details', kwargs={'slug':slug}))


    return render(request, 'Blog/blog_details.html', context={'blog':blog,'comment_form':comment_form,'liked':liked})    

@login_required
def liked(request, id):
    blog =Blog.objects.get(pk=id)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog,user=user)
    if not already_liked:
        liked_post = Likes(blog=blog, user=user)
        liked_post.save()

    return HttpResponseRedirect(reverse('Blog:blog_details', kwargs={'slug':blog.slug}))

@login_required
def unliked(request, id):
    blog =Blog.objects.get(pk=id)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog,user=user)
    if  already_liked:
        already_liked.delete()

    return HttpResponseRedirect(reverse('Blog:blog_details', kwargs={'slug':blog.slug}))
     
    
class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'Blog/my_blog.html'

class EditBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title','blog_contain','blog_image')
    template_name = 'Blog/edit_blog.html'

    def get_success_url(self,  **kwargs):
        return reverse_lazy('Blog:blog_details', kwargs={'slug':self.object.slug})




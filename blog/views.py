from mimetypes import init
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm


# from django.urls import reverse
# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'
    
    def get_queryset(self):
        return super().get_queryset().order_by('id')[:3]


class AllPostsView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    ordering = ['-id']
    context_object_name = 'all_posts'

class PostView(View):
    def get(self, request, slug):
        current_post = get_object_or_404(Post, slug=slug)
        form = CommentForm()
        
        return self.render_post_detail(request, current_post, form, slug)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        current_post = get_object_or_404(Post, slug=slug)
        if form.is_valid():
            post = form.save(commit=False)
            post.post = current_post
            post.save()
            return HttpResponseRedirect(reverse('blog_specific', args=[slug]))
        return self.render_post_detail(request, current_post, form, slug)
    
    
    def render_post_detail(self, request, post, form, slug):
        # print(request.session.get('favorite-posts'))
        return render(request, 'blog/post_detail.html', {
            'post': post,
            'post_tags': post.tags.all(),
            'comments': post.comment_set.all().order_by('-date'),
            'form': form,
            'is_favorite': self.is_favorite(request, slug)
        })
    
    def is_favorite(self, request, slug):
        if request.session['favorite-posts'] and slug in request.session['favorite-posts']: 
            return True
        return False
        

class FavPostsView(View):
    def get(self, request):
        fav_slugs_list = request.session['favorite-posts'].keys() if request.session['favorite-posts'] else []
        fav_posts = Post.objects.filter(slug__in=fav_slugs_list)
        return render(request,'blog/favorite_posts.html',{
            'favorite_posts': fav_posts
        })
        
        
class AddORemoveFavPost(View):
    def post(self, request):
        post_slug = request.POST.get('post_slug')
        is_favorite = request.POST.get('is_favorite_post')
        fav_posts = request.session.get('favorite-posts')
        if is_favorite == 'True':
            fav_posts.pop(post_slug)
        else:
            if fav_posts:
                fav_posts[post_slug] = True
                print(post_slug)
            else:
                fav_posts = {post_slug: True}
        request.session['favorite-posts'] = fav_posts
        return HttpResponseRedirect(reverse('blog_specific', args=[post_slug]))

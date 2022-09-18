from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='blog_index'),
    path('posts', views.AllPostsView.as_view(), name='blog_posts'),
    path('posts/favorite-posts', views.FavPostsView.as_view(), name='favorite-posts'),
    path('posts/add-or-remove-favorite', views.AddORemoveFavPost.as_view(), name='fav-control'),
    path('posts/<slug:slug>', views.PostView.as_view(), name='blog_specific')
]

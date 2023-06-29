from django.urls import path
from .views import CreatePost, PostDetail, ViewAllPosts


urlpatterns = [
    path('post/new', CreatePost.as_view(), name="add-post"),
    path('post/<int:id>', PostDetail.as_view(), name="detail-post"),
    path('posts/', ViewAllPosts.as_view(), name="list-posts")
    ]
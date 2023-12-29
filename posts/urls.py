from django.urls import path
from .views import PostDetail, PostList

app_name = 'posts'

urlpatterns = [
    path('<int>:pk)', PostDetail.as_view(), name='post_detail'),
    path("", PostList.as_view(), name="post_list"),
]

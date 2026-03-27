from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog_home'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
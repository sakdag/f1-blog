from django.urls import path

from apps.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='all'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('by/<str:username>/', views.UserPosts.as_view(), name='for_user'),
    path('by/<str:username>/<int:pk>/', views.PostDetail.as_view(), name='single'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete')
]
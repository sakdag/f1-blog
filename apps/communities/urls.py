from django.urls import path

from apps.communities import views

app_name = 'communities'

urlpatterns = [
    path('', views.ListCommunities.as_view(), name='list_communities'),
    path('create/', views.CreateCommunity.as_view(), name='create_community'),
    path('posts/in/<slug:slug>/', views.SingleCommunity.as_view(), name='single_community'),
]
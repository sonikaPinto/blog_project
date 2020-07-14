from django.urls import path
from blog import views

urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_create'),
    path('post/edit/<int:pk>/',views.UpdatePostView.as_view(),name='post_update'),
    path('post/remove/<int:pk>/',views.DeletePostView.as_view(),name='post_delete'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft'),
    path('post/<int:pk>/comment/',views.add_comment_post,name='comment_create'),
    path('post/comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('post/comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),

]

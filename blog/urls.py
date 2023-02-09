from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/likes/', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/dislikes/', views.DisLike.as_view(), name='add_dislikes'),
]

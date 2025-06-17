from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('<int:yr>/<int:mn>/<int:dy>/<slug:slug>/',views.post_detail,name='post_detail'),
    path('<int:id>/share/',views.post_share,name='post_share')
    # path('<int:id>/<slug:slug>/',views.post_detail,name='post_detail')
]

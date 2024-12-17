from django.urls import path

from myBlog import views

urlpatterns = [
    path('', views.PostList.as_view(), name="post_list"),
    path('archives/', views.ArchiveList.as_view(), name="archive_list"),
    path('search/', views.SearchList.as_view(), name="search_list"),
    path('<slug:category_slug>/<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/',views.CategoryList.as_view(), name='category_list')
]

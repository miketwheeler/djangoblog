from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('questing/', views.Questing.as_view(), name="questing"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
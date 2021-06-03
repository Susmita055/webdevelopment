from django.urls import path
from . import views

urlpatterns = [
    #path('blog/', views.post_list,name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('', views.index, name='index'), 
    path('post_list/', views.post_list, name='post_list'),
    #path('post/new/post/', views.post_list, name='post_list'),
    path('title_upload', views.upload, name='upload'),
    path('email/', views.subscribe, name='submit'),
    path('fetch/',views.fetch, name='save'),
    path('mass/',views.mass_mail, name='save'),
    path('attach/',views.attach, name='save'),
    path('home/',views.home, name='save'),
]



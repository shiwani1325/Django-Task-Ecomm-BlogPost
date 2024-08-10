
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('blogpost/<str:pk>/',views.blogpostview,name='blogpostview'),
    path('blogpost-add/',views.blogpostadd,name='blogpostadd'),
    path('blogpost-update/<str:pk>/',views.blogpostupdate,name='blogpostupdate'),
    path('blogpost-delete/<str:pk>/',views.blogpostdelete,name='blogpostdelete'),
]

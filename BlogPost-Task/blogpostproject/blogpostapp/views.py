from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BlogPost
from .serializers import BlogPostSerializer
# Create your views here.


@api_view(['GET'])
def index(request):
    blog=BlogPost.objects.all()
    serialblogs=BlogPostSerializer(blog,many=True)
    return Response(serialblogs.data)

@api_view(['GET'])
def blogpostview(request,pk):
    blog=BlogPost.objects.get(id=pk)
    serialblog=BlogPostSerializer(blog,many=False)
    return Response(serialblog.data)
    
    
    
@api_view(['POST'])
def blogpostadd(request):
    serialdataadd=BlogPostSerializer(data=request.data)
    if serialdataadd.is_valid():
        serialdataadd.save()
    return Response(serialdataadd.data)
    
    
@api_view(['POST'])
def blogpostupdate(request,pk):
    blog=BlogPost.objects.get(id=pk)
    serialblog=BlogPostSerializer(instance=blog, data=request.data)

    if serialblog.is_valid():
        serialblog.save()
    return Response(serialblog.data)
        
    
@api_view(['DELETE'])   
def blogpostdelete(request,pk):
    blog=BlogPost.objects.get(id=pk)
    blog.delete()
    
    blog=BlogPost.objects.all()
    serialblogs=BlogPostSerializer(blog,many=True)
    return Response(serialblogs.data)

    
    
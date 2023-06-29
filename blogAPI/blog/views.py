from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from blog.models import Post
from blog.serializers import PostSerializer



class CreatePost(generics.GenericAPIView):
    serializer_class = PostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
             serializer.save()
        return Response({"message": f"{serializer.data['title']} created successfully"}, status=status.HTTP_201_CREATED)



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "id"


    def get_queryset(self):
        return super().get_queryset()

class ViewAllPosts(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return super().get_queryset()
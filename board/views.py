from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Post의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능

class PostViewSet(viewsets.ModelViewSet):
    # authentication 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

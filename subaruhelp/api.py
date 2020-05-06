from rest_framework.viewsets import ModelViewSet
from rest_framework import routers
from .models import ObdCode, Comment
from .serializers import ObdCodeSerializer, CommentSerializer


class ObdCodeViewSet(ModelViewSet):
    serializer_class = ObdCodeSerializer
    queryset = ObdCode.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

router = routers.SimpleRouter()
router.register(r'obdcodes', ObdCodeViewSet)
router.register(r'comments', CommentViewSet)
api_urls = router.urls

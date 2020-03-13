from authors.views import AuthorsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(
    r'authors',
    AuthorsViewSet
)

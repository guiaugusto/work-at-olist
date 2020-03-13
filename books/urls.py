from books.views import BooksViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(
    r'books',
    BooksViewSet
)

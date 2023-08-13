from rest_framework.routers import DefaultRouter

from books.views import BookEndPoint

router = DefaultRouter(trailing_slash=False)

router.register("books", BookEndPoint, basename="books")

urlpatterns = router.urls

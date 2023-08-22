from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.Reviews.as_view(),
        name="reviews",
    ),
    path(
        "category_reviews/<str:category>/",
        views.CategoryReviewList.as_view(),
        name="category-review-list",
    ),
]

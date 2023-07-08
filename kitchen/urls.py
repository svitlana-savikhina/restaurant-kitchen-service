from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "cooks/", CookListView.as_view(),
        name="cook-list",
    ),
    path(
        "cooks/<int:pk>/", CookDetailView.as_view(),
        name="cook-detail",
    ),
    path(
        "cooks/create/", CookCreateView.as_view(),
        name="cook-create"
    ),
    path(
        "cooks/<int:pk>/update/", CookUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cooks/<int:pk>/delete/", CookDeleteView.as_view(),
        name="cook-delete"
    ),
    path(
        "dishes/", DishListView.as_view(),
        name="dish-list",
    ),
]

app_name = "kitchen"

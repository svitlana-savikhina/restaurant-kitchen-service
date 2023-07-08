from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView, DishUpdateView, DishDeleteView, AssignToDishView, DishTypeListView,
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
    path(
        "dishes/<int:pk>/", DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dishes/create/", DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dishes/<int:pk>/update/", DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete/", DishDeleteView.as_view(),
        name="dish-delete",
    ),
    path(
        "dishes/<int:pk>/assigning/", AssignToDishView.as_view(),
        name="cook-assigning",
    ),
    path(
        "dish_types/", DishTypeListView.as_view(),
        name="dish-type-list"
    ),
]

app_name = "kitchen"

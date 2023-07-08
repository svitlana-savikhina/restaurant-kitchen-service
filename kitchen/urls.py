from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    CookDetailView,
    CookCreateView,
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
]

app_name = "kitchen"

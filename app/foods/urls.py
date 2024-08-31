from django.urls import path

from . import views

urlpatterns = [
    path("", views.FoodListView.as_view(), name="food-list"),
    path("detail/<int:pk>/", views.FoodDetailView.as_view(), name="food-detail"),
    path("food-liked/", views.FoodLikedListView.as_view(), name="food-liked"),
    path(
        "food-week-plan/", views.FoodWeekPlanListView.as_view(), name="food-week-plan"
    ),
    path("food-choices/", views.food_choice_list_view, name="food-choices"),
]

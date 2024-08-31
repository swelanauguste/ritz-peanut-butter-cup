from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from .forms import FoodUpdateForm
from .models import Family, Food, Group


def food_choice_list_view(request):
    # Get selected food IDs from the request
    food1_id = request.GET.get("food1")
    food2_id = request.GET.get("food2")
    food3_id = request.GET.get("food3")
    food4_id = request.GET.get("food4")

    # Initial queryset for all foods
    queryset = Food.objects.all()

    # Filter by the family of the selected food, if any food is selected
    if food1_id:
        family1 = Food.objects.get(id=food1_id).family
        queryset = queryset.filter(family=family1)

    if food2_id:
        family2 = Food.objects.get(id=food2_id).family
        queryset = queryset.filter(family=family2)

    if food3_id:
        family3 = Food.objects.get(id=food3_id).family
        queryset = queryset.filter(family=family3)

    if food4_id:
        family4 = Food.objects.get(id=food4_id).family
        queryset = queryset.filter(family=family4)

    # Prepare the context for rendering
    context = {
        "choice1": Food.objects.all(),
        "choice2": Food.objects.all(),
        "choice3": Food.objects.all(),
        "choice4": Food.objects.all(),
        "selected_food1": food1_id,
        "selected_food2": food2_id,
        "selected_food3": food3_id,
        "selected_food4": food4_id,
        "food_list1": (
            Food.objects.filter(family__name=family1.name)
            if food1_id
            else Food.objects.all()
        ),
        "food_list2": (
            Food.objects.filter(family__name=family2.name)
            if food2_id
            else Food.objects.all()
        ),
        "food_list3": (
            Food.objects.filter(family__name=family3.name)
            if food3_id
            else Food.objects.all()
        ),
        "food_list4": (
            Food.objects.filter(family__name=family4.name)
            if food4_id
            else Food.objects.all()
        ),
    }
    return render(request, "foods/food_choice_list.html", context)





class FoodWeekPlanListView(ListView):
    model = Food
    template_name = "foods/food_week_plan_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["week1"] = Food.objects.filter(add_to_week_plan__week="week1")
        context["week2"] = Food.objects.filter(add_to_week_plan__week="week2")
        context["week3"] = Food.objects.filter(add_to_week_plan__week="week3")
        context["week4"] = Food.objects.filter(add_to_week_plan__week="week4")
        context["week5"] = Food.objects.filter(add_to_week_plan__week="week5")
        return context


class FoodLikedListView(ListView):
    model = Food
    template_name = "foods/food_liked_list.html"

    queryset = Food.objects.filter(like=True)


class FoodListView(ListView):
    model = Food
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_allergic=False)
        week_plan = self.request.GET.get("week_plan")
        search_query = self.request.GET.get("q")

        if week_plan:
            queryset = queryset.filter(
                add_to_week_plan__week=week_plan, is_allergic=False
            )

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(family__icontains=search_query)
                | Q(friendly_family_name__icontains=search_query)
                | Q(group__icontains=search_query)
                | Q(tags__name__icontains=search_query),
                is_allergic=False,
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "")
        context["family_list"] = Family.objects.all()
        return context


class FoodDetailView(DetailView):
    model = Food

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        food = self.get_object()

        # Get related foods based on the group and family
        related_foods = Food.objects.filter(family=food.family).exclude(pk=food.pk)
        # related_foods = (
        #     Food.objects.filter(family=food.family).exclude(pk=food.pk)
        #     .order_by("family")
        #     # .order_by("family")[:5]
        # )  # Exclude the current food item

        if self.request.method == "POST":
            form = FoodUpdateForm(self.request.POST, instance=food)
            if form.is_valid():
                form.save()
                return redirect("food-detail", pk=food.pk)  # Update with your URL name
        else:
            form = FoodUpdateForm(instance=food)

        context["form"] = form
        context["related_foods"] = related_foods
        return context

    def post(self, request, *args, **kwargs):
        food = self.get_object()
        form = FoodUpdateForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect("food-detail", pk=food.pk)  # Update with your URL name
        return render(request, self.template_name, {"food": food, "form": form})
        return render(request, self.template_name, {"food": food, "form": form})

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from .forms import FoodUpdateForm
from .models import Food


from django.views.generic import ListView
from .models import Food

class FoodChoiceListView(ListView):
    model = Food
    template_name = "foods/food_choice_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        family = self.request.GET.get('family')

        if family:
            queryset = queryset.filter(family=family)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get a list of unique family names
        context['unique_families'] = Food.objects.values_list('family', flat=True).distinct()
        context['current_family'] = self.request.GET.get('family', '')
        return context



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
        return context


class FoodDetailView(DetailView):
    model = Food

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        food = self.get_object()

        # Get related foods based on the group and family
        related_foods = (
            Food.objects.filter(Q(family=food.family))
            .exclude(pk=food.pk)
            .order_by("family")
            # .order_by("family")[:5]
        )  # Exclude the current food item

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

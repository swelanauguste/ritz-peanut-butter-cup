from django.db import models
from users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class WeekPlan(models.Model):
    week = models.CharField(max_length=5, unique=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)

    class Meta:
        ordering = ["week"]

    def __str__(self):
        return self.week


class Family(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "families"

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "families"

    def __str__(self):
        return self.name


class Food(models.Model):
    like = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='foods', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='foods', null=True, blank=True)
    is_allergic = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    add_to_week_plan = models.ManyToManyField(WeekPlan, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.is_allergic:
            return f"allergic to {self.name}"
        return self.name

from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    avatar = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def user_count(self):
        return self.archteamsqnauser_set.count()


class ArchTeamsQnaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)
    full_name = models.CharField(max_length=250, blank=False, null=False)
    avatar = models.CharField(max_length=50, blank=True, null=True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name + ' [user: ' + self.user.username + ']'


class Tag(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

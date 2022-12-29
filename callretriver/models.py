from django.db import models

# Create your models here.


class Company(models.Model):
    company_parent = models.ForeignKey(
        'self',
        related_name="company_child",
        blank=False,
        null=True,
        on_delete=models.CASCADE,
        default=None
    )
    name = models.CharField(max_length=255, blank=False, null=False)


class Team(models.Model):
    company_parent = models.ForeignKey(
        Company,
        related_name="company_team_child",
        blank=False,
        null=True,
        on_delete=models.CASCADE,
        default=None
    )
    team_parent = models.ForeignKey(
        'self',
        related_name="team_child",
        blank=False,
        null=True,
        on_delete=models.CASCADE,
        default=None
    )
    name = models.CharField(max_length=255, blank=False, null=False)


class User(models.Model):
    company_parent = models.ForeignKey(
        Company,
        related_name="company_user_child",
        blank=False,
        null=True,
        on_delete=models.CASCADE,
        default=None
    )
    team_parent = models.ForeignKey(
        Team,
        related_name="team_user_child",
        blank=False,
        null=True,
        on_delete=models.CASCADE,
        default=None
    )
    name = models.CharField(max_length=255, blank=False, null=False)


class Call(models.Model):
    data = models.CharField(max_length=255, blank=False, null=False)
    owner = models.ForeignKey(
        User,
        related_name="call_owner",
        blank=False,
        null=True,
        on_delete=models.CASCADE
    )

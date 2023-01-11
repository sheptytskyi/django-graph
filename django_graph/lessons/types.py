import strawberry
from django.contrib.auth import get_user_model
from strawberry import auto
from typing import List
from . import models


@strawberry.django.type(get_user_model())
class UserType:
    username: auto
    first_name: auto
    last_name: auto


@strawberry.django.type(models.Hall)
class Hall:
    id: auto
    city: auto
    street: auto


@strawberry.django.type(models.Member)
class Member:
    id: auto
    is_coach: auto
    user: UserType


@strawberry.django.type(models.Lesson)
class Lessons:
    id: auto
    hall: Hall
    members: List[Member]

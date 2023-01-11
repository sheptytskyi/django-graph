import strawberry
from typing import List
from .types import Lessons


@strawberry.type
class Query:
    lessons: List[Lessons] = strawberry.django.field()


schema = strawberry.Schema(query=Query)

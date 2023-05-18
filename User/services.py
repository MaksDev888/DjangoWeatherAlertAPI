from django.db.models import QuerySet

from User.models import UserApp


def get_all_users() -> QuerySet:
    return UserApp.objects.all()

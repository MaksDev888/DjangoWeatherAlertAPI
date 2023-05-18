from django.db import models

from User.models import UserApp
from City.models import City


class FollowList(models.Model):
    HOURS = (
        (1, 1),
        (3, 3),
        (6, 6),
        (12, 12),
    )

    user_id = models.ForeignKey(
        UserApp,
        on_delete=models.CASCADE,
        related_name="subscriprions_user",
        verbose_name="User",
    )
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name="subscriprions", verbose_name="City id")

    created = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Created")
    send_time_email = models.SmallIntegerField(default=1, choices=HOURS, verbose_name="Send time email")

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
        unique_together = ("user_id", "city_id")
        ordering = ["-created"]

    def __str__(self) -> str:
        return f"{self.user_id} - {self.city_id}"

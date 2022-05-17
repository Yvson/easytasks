from django.db import models
from django.db.models import Count
from django.core.exceptions import ValidationError
from conta.models import Profile


class Color(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile,
                                related_name='colors',
                                on_delete=models.CASCADE)
    color = models.CharField(max_length=7, blank=False)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
        ordering = ["-date"]

    def __str__(self):
        return f'Colors for user {self.profile.user.username}'
    
    def save(self, *args, **kwargs):
        profile_colors = Profile.objects.filter(id=self.profile.id).annotate(qty_entries=Count('colors'))
        if profile_colors[0].qty_entries >= 18:
            raise ValidationError(
                'Exceeded maximum limit of entries',
                code='Exceeded limit')
        super().save(self, *args, **kwargs)

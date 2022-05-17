from django.db import models
from conta.models import Profile
from django.db.models import Count
from django.core.exceptions import ValidationError


class Number(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile,
                                related_name='numbers',
                                on_delete=models.CASCADE)
    numbers = models.TextField(blank=False)
    columns = models.IntegerField(blank=False)

    class Meta:
        verbose_name = 'Number'
        verbose_name_plural = 'Numbers'
        ordering = ["-date"]

    def __str__(self):
        return f'Numbers for user {self.profile.user.username}'

    def save(self, *args, **kwargs):
        profile_numbers = Profile.objects.filter(id=self.profile.id).annotate(qty_entries=Count('numbers'))
        if profile_numbers[0].qty_entries >= 15:
            raise ValidationError(
                'Exceeded maximum limit of entries',
                code='Exceeded limit')
        super().save(self, *args, **kwargs)


class Password(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile,
                                related_name='passwords',
                                on_delete=models.CASCADE)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'
        ordering = ["-date"]

    def __str__(self):
        return f'Passwords for user {self.profile.user.username}'

    def save(self, *args, **kwargs):
        profile_passwords = Profile.objects.filter(id=self.profile.id).annotate(qty_entries=Count('passwords'))
        if profile_passwords[0].qty_entries >= 15:
            raise ValidationError(
                'Exceeded maximum limit of entries',
                code='Exceeded limit')
        super().save(self, *args, **kwargs)


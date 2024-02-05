from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Publication, Vote
import random


@receiver(post_migrate)
def create_first_data(sender, **kwargs):
    # creating some data in an empty db during migration
    if sender.name == 'publications':
        if User.objects.count() == 0:
            User.objects.create_superuser('admin', 'admin@admin.com', 'a1d2m3i4n5')
            for i in range(1, 11):
                username = f'user_{i}'
                User.objects.create_user(username, f'{username}@{username}.com', f'12qwaszx{i}')

        if Publication.objects.count() == 0 and Vote.objects.count() == 0:
            publication_text = 'This is the text of the publication number {number}!'
            for i in range(1, 11):
                user = User.objects.get(username=f'user_{i}')
                Publication.objects.create(text=publication_text.format(number=i), author=user)
                Publication.objects.create(text=publication_text.format(number=i + 10), author=user)

            for i in range(1, 11):
                user = User.objects.get(username=f'user_{i}')
                for j in range(1, 21):
                    publication = Publication.objects.get(text=publication_text.format(number=j))
                    Vote.objects.create(user=user, publication=publication, value=random.choice([-1, 0, 1]))

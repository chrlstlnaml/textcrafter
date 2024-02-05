from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    text = models.TextField()
    public_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username} ({self.public_date})'

    class Meta:
        db_table = 'publication'


class PublicationView(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    public_date = models.DateTimeField()
    author_id = models.IntegerField()
    author = models.CharField(max_length=150)
    rating = models.IntegerField()
    vote_count = models.IntegerField()

    def __str__(self):
        return f'{self.author} {self.text}'

    class Meta:
        managed = False
        db_table = 'vw_publication'


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=[(1, 'Like'), (0, 'Revoke'), (-1, 'Dislike')], default=0)

    def __str__(self):
        return f'{self.user.name} {self.publication} {self.value}'

    class Meta:
        unique_together = ('user', 'publication')
        db_table = 'vote'

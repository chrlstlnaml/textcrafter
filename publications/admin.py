from django.contrib import admin
from .models import Publication, Vote, PublicationView


admin.site.register(Publication)
admin.site.register(PublicationView)
admin.site.register(Vote)

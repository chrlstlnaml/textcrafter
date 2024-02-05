from django.urls import path
from .views import PublicationList, PublicationCreate, VoteUpdate

urlpatterns = [
    path('publication/', PublicationList.as_view(), name='publication-list'),
    path('publication/create/', PublicationCreate.as_view(), name='create-publication'),
    path('publication/vote/', VoteUpdate.as_view(), name='vote-for-publication'),
]
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Vote, PublicationView
from .serializers import PublicationSerializer, VoteSerializer, PublicationViewSerializer
from django.db import transaction
from rest_framework.views import APIView


class PublicationList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        order_by = self.request.query_params.get('order_by', None)
        ORDERING = {
            'latest': '-public_date',
            'top_rated': '-rating'
        }

        if order_by in ORDERING:
            publications = PublicationView.objects.all().order_by(ORDERING[order_by], 'text')[:10]
            serializer = PublicationViewSerializer(publications, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise ValidationError({'order_by': 'This parameter is required.'})


class PublicationCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request, format=None):
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    VOTE_VALUES = {
        'like': 1,
        'dislike': -1,
        'revoke': 0
    }

    @transaction.atomic
    def post(self, request, format=None):
        serializer = VoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        publication_id = request.data.get('publication')
        value = request.data.get('value')

        vote, created = Vote.objects.get_or_create(user=request.user, publication_id=publication_id)
        vote.value = self.VOTE_VALUES[value]
        vote.save()

        return Response({'message': 'Vote has been updated successfully'}, status=status.HTTP_200_OK)

from rest_framework import generics

from tips.models import Tip
from .serializers import TipSerializer
from .permissions import IsOwnerOrReadOnly


class TipList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all tips in the DB.

    post:
    Create an awesome new tip.
    """
    queryset = Tip.objects.all()
    serializer_class = TipSerializer


class TipDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return an individual tip.

    put:
    Update an existing tip.

    delete:
    Delete a single tip.
    """
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

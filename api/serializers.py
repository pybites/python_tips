from rest_framework import serializers

from tips.models import Tip


class TipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tip
        fields = ('tip', 'code', 'link', 'user', 'approved', 'share_link')

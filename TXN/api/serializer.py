from rest_framework import serializers
from txn.models import TXN


class TXNSerializer(serializers.ModelSerializer):
    class Meta:
        model = TXN
        fields = '__all__'
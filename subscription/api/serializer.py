from rest_framework import serializers
from subscription.models import GymMemberShip, Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ['is_active', 'created_at', 'updated_at']

class GymMemberShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymMemberShip
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
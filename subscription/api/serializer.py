from rest_framework import serializers
from subscription.models import GymMemberShip, Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ['is_active', 'created_at', 'updated_at']

class GymMemberShipSerializer(serializers.ModelSerializer):
    price  = serializers.IntegerField(read_only=True)
    class Meta:
        model = GymMemberShip
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['subscription'] = instance.subscription.name
        data['member'] = instance.member.first_name + ' ' + instance.member.last_name
        data['trainer'] = instance.trainer.full_name if instance.trainer is not None else None
        return data

    def create(self, validated_data):
        print(validated_data)
        one_day_price = validated_data['subscription'].price / validated_data['subscription'].days
        validated_data['price']=validated_data['days']*one_day_price
        return super().create(validated_data)
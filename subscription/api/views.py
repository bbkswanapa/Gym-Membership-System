from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from subscription.api.serializer import GymMemberShipSerializer, SubscriptionSerializer
from subscription.models import GymMemberShip, Subscription
from txn.models import TXN, Status
from django.db import transaction
from subscription.api.service import khalti_payment


class SubscriptionView(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get(self, request):
        subscription = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        data = request.data
        serializer = SubscriptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Subscription created successfully",
                },
                201,
            )
        else:
            return Response(serializer.errors, 422)


class SubscriptionUpdateAndDelete(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def put(self, request, pk):
        subscription = Subscription.objects.get(id=pk)
        data = request.data
        serializer = SubscriptionSerializer(subscription, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Subscription updated successfully",
                },
                200,
            )
        else:
            return Response(serializer.errors, 422)

    def delete(self, request, pk):
        subscription = Subscription.objects.filter(id=pk)
        subscription.delete()
        return Response(
            {
                "message": "Subscription deleted successfully",
            },
            200,
        )

@extend_schema(
    request=GymMemberShipSerializer,
    responses=GymMemberShipSerializer,
    tags=['GymMemberShip']
)


class GymMemberShipView(GenericAPIView):
    queryset = GymMemberShip.objects.all()
    serializer_class = GymMemberShipSerializer

    def get(self, request):
        data = GymMemberShip.objects.all()
        serializer = GymMemberShipSerializer(data, many=True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        data = request.data
        serializer = GymMemberShipSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "GymMemberShip created successfully"}, 201)
        else:
            return Response(serializer.errors, 422)
        
class MembershipPayment(GenericAPIView):
    queryset = GymMemberShip.objects.all()
    serializer_class = []

    @transaction.atomic
    def get(self,request,id):
        data = GymMemberShip.objects.get(id=id)
        txn = TXN.objects.create(
            member = data.member,
            name = f'{data.member.first_name}-"Upgrade"',
            amount = data.price
        )
    
        result = khalti_payment(data.member,txn)
        if 'error' not in result:
            txn.pidx = result['pidx']
            txn.status = Status.KHALTI_PROCESS
            txn.save()

        return Response(result)
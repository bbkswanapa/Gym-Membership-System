from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


from subscription.api.serializer import SubscriptionSerializer
from subscription.models import Subscription


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

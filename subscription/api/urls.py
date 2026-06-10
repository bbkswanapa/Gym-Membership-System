from django.urls import path
from subscription.api.views import  MembershipPayment, SubscriptionView, SubscriptionUpdateAndDelete ,GymMemberShipView
urlpatterns = [
    path('', SubscriptionView.as_view(), name='subscription'),
    path('<int:pk>/', SubscriptionUpdateAndDelete.as_view(), name='subscription-update-delete'),
    path('member/', GymMemberShipView.as_view(), name='gymmembership'),
    path('payment/<int:id>/',MembershipPayment.as_view()),

]
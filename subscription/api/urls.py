from django.urls import path
from subscription.api.views import  SubscriptionView, SubscriptionUpdateAndDelete ,GymMemberShipView
urlpatterns = [
    path('', SubscriptionView.as_view(), name='subscription'),
    path('<int:pk>/', SubscriptionUpdateAndDelete.as_view(), name='subscription-update-delete'),
    path('member/', GymMemberShipView.as_view(), name='gymmembership'),

]
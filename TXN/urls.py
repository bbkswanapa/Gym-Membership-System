from django.urls import path

from txn.views import callback_view

urlpatterns = [
    # Exercise Category
    path('callback/',callback_view),
]
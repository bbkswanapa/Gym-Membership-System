from django.shortcuts import render
from txn.models import TXN,Status
from subscription.models import Subscription, GymMemberShip

# Create your views here.


def callback_view(request):
    data = request.GET
    print(data['pidx'])
    txn = TXN.objects.get(pidx=data['pidx'])
    if data['status']=="Completed":
        txn.status =Status.COMPLETED
        txn.txn_id = data['tidx']
        member_ship = GymMemberShip.objects.get(member=txn.member)
        sub = member_ship.subsrciption
        member_ship.days = member_ship.days + sub.days
        member_ship.member.is_active = True
        member_ship.save()
    elif data['status']=="Pending":
        txn.status == Status.PENDING
    else:
        txn.status = Status.USER_CANCELED
    txn.save()
    return render(request,'txn/index.html', {'txn':txn})
from celery import shared_task
from member.models import Member
from attendance.models import Attendance
from datetime import datetime

@shared_task
def add_attendace():
    member = Member.objects.filter(is_active=True)
    for i in member:
        attendance = Attendance.objects.create(
            member=i,
            attendance_date=datetime.now().date()
        )
    return True


@shared_task
def mark_member_attendance():
    attendance = Attendance.objects.all()
    for i in attendance:
        if i.check_in :
            i.is_present = True
            if not i.check_out:
                i.check_out = datetime.now().time()
            i.save(update_fields=['check_out', 'is_present'])
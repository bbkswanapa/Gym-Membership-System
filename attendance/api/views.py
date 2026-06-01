from attendance.api.serializer import AttendanceSerializer
from attendance.models import Attendance

from rest_framework.generics import GenericAPIView
from rest_framework import response


class AttendanceView(GenericAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def patch(self, request, *args, **kwargs):
        return response ({
            "message" : "Patch Request"
         })
 
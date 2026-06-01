from django.urls import path
from attendance.api.views import AttendanceView


urlpatterns = [
     path('update/<int:pk>/', AttendanceView.as_view(), name='attendance-update'),
]
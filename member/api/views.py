from drf_spectacular.utils import extend_schema
from rest_framework import status

from member.tasks import mark_all_member_active
from member.models import Member
from member.api.serializer import MemberSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@extend_schema(
        responses=MemberSerializer
)

@api_view(['GET'])
def memberlist(request):
    data = Member.objects.all()
    mark_all_member_active.delay() #calling the celery task to mark all members as active
    serializer = MemberSerializer(data, many=True)
    return Response(serializer.data)

@extend_schema(
        request=MemberSerializer,
        responses=MemberSerializer,
        tags = ["Test"] #tags are used to group the APIs in the documentation
)

@api_view(['POST'])
def membercreate(request):
    post_data = request.data
    serializer = MemberSerializer(data=post_data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Member created successfully",
        }, status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

@extend_schema(
        request=MemberSerializer,
        responses=MemberSerializer
)

@api_view(['PUT'])
def memberupdate(request, id):
    member = Member.objects.get(id=id)
    serializer = MemberSerializer(member, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Member updated successfully",
        }, status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    
@extend_schema(
        request=MemberSerializer
)
    
@api_view(['DELETE'])
def memberdelete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return Response({
        "message": "Member deleted successfully",
    }, status.HTTP_204_NO_CONTENT)

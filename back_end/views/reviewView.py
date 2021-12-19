from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from back_end.models import Course
from back_end.serializers import ReviewSerializer


class AddReview(APIView):
    def post(self, request, courseId, *args, **kwargs):
        user = request.user

        if user.category == 0:
            return Response({"error": "The user is not creator."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            if not Course.objects.filter(pk=courseId).exists():
                return Response({"error": "The course does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({}, status=status.HTTP_200_OK)
            return Response({"error": "Could not create the review."}, status=status.HTTP_400_BAD_REQUEST)
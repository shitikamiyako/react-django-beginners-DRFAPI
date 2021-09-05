from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .own_permissions import ProfilePermission

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):

    queryset =  User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ProfilePermission,)


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
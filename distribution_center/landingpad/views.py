from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from rest_framework import viewsets, permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
from .models import Rma
from rest_framework_simplejwt.tokens import RefreshToken
#from django.core.mail import send_mail
#from .serializers import RmaSerializer

#send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)

class RmaViewSet(viewsets.ModelViewSet):
    queryset = Rma.objects.all()
    serializer_class = RmaSerializer
    classes = (TokenHasReadWriteScope, OAuth2Authentication)

from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework.response import response

class RegisterView(generics.GenericAPIView):

    serializer_class=RegisterSerializer

    def post(self, request):
        user=request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data=serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)





    

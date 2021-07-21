from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from rest_framework import viewsets, permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
from .models import Rma
#from .serializers import RmaSerializer

class RmaViewSet(viewsets.ModelViewSet):
    queryset = Rma.objects.all()
    serializer_class = RmaSerializer
    classes = (TokenHasReadWriteScope, OAuth2Authentication)
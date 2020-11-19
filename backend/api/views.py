from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer
# from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


@api_view(['POST'])
def login(request):
    """
    Get the username and password from the request.data and check whether correct.
    """
    if request.method == 'POST':
        # serializer = AccountSerializer(data=request.data)
        # if serializer.is_valid():
        data = JSONParser().parse(request)
        print(data)
        try:
            account = Account.objects.get(username=data['username'])
        except Account.DoesNotExist:
            print("Oh shit, account not found")
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            if account.password != data['password']:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                serializer = AccountSerializer(account)
                return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

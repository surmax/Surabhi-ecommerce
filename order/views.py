from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer
from .authentication import get_user_info
from djoser.conf import User 
from djoser.serializers import UserSerializer



@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
def checkout(request):
    user_info = get_user_info(request)
    if (user_info): # If the user is legit 
        user_serializer = UserSerializer(data=user_info['given_name'])

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])
            #serializer.save(user=user_info, paid_amount=paid_amount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Not a valid user based on the Bearer Token'}, status=status.HTTP_401_UNAUTHORIZED)




class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)

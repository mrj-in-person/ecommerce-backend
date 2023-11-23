from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from user import models as user_models
from product import models as product_models
from cart import models as cart_models
from order import models as order_models
from rest_framework import generics
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


# users views
class UsersList(APIView):
    permission_classes = [AllowAny]

    def get_queryset(self):
        users = user_models.CustomUser.objects.all()
        return users

    def get(self, request, *args, **kwargs):
        
        id = request.query_params["id"]
        user = user_models.CustomUser.objects.get(id=id)
        
        users = self.get_queryset()
        serializer = serializers.CustomUserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # data = request.data
        # new_user = user_models.CustomUser.objects.create_user(
        #     username=data.get("username"),
        #     first_name=data.get("first_name"),
        #     last_name=data.get("last_name"),
        #     email=data.get("email"),
        #     password=data.get("password"),
        #     phone=data.get("phone"),
        # )
        # serializer = serializers.CustomUserSerializer(new_user)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     raise Response(serializer.errors)
        serializer = serializers.CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
    permission_classes = [AllowAny]


class SocialProfileList(generics.ListCreateAPIView):
    queryset = user_models.SocialProfile.objects.all()
    serializer_class = serializers.SocialProfileSerializer
    permission_classes = [AllowAny]


class SocialProfileRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_models.SocialProfile.objects.all()
    serializer_class = serializers.SocialProfileSerializer
    permission_classes = [AllowAny]


class CredentialsList(generics.ListCreateAPIView):
    queryset = user_models.Credentials.objects.all()
    serializer_class = serializers.CredentialsSerializer
    permission_classes = [AllowAny]


class CredentialsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_models.Credentials.objects.all()
    serializer_class = serializers.CredentialsSerializer
    permission_classes = [AllowAny]


# product views
class ProductList(generics.ListAPIView):
    queryset = product_models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [AllowAny]


class ProductRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [AllowAny]


class CategoriesList(generics.ListCreateAPIView):
    queryset = product_models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [AllowAny]


class CategoriesRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [AllowAny]


class ReviewList(generics.ListCreateAPIView):
    queryset = product_models.Reviews.objects.all()
    serializer_class = serializers.ReviewsSerializer
    permission_classes = [AllowAny]


class ReviewRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Reviews.objects.all()
    serializer_class = serializers.ReviewsSerializer
    permission_classes = [AllowAny]


# order views
class OrderList(generics.ListCreateAPIView):
    queryset = order_models.Orders.objects.all()
    serializer_class = serializers.OrdersSerializer
    permission_classes = [AllowAny]


class OrderRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = order_models.Orders.objects.all()
    serializer_class = serializers.OrdersSerializer
    permission_classes = [AllowAny]


class OrderLinesList(generics.ListCreateAPIView):
    queryset = order_models.OrderLines.objects.all()
    serializer_class = serializers.OrderLinesSerializer
    permission_classes = [AllowAny]


class OrderLinesRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = order_models.OrderLines.objects.all()
    serializer_class = serializers.OrderLinesSerializer
    permission_classes = [AllowAny]


# cart views
class CartsList(generics.ListCreateAPIView):
    queryset = cart_models.Carts.objects.all()
    serializer_class = serializers.CartsSerializer
    permission_classes = [AllowAny]


class CartsRetieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = cart_models.Carts.objects.all()
    serializer_class = serializers.CartsSerializer
    permission_classes = [AllowAny]


class CartItemsList(generics.ListCreateAPIView):
    queryset = cart_models.CartItems.objects.all()
    serializer_class = serializers.CartItemsSerializer
    permission_classes = [AllowAny]


class CartItemsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = cart_models.CartItems.objects.all()
    serializer_class = serializers.CartItemsSerializer
    permission_classes = [AllowAny]

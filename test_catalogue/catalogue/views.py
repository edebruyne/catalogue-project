from .models import *
from .serializer import *
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

 

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
	    return Product.objects.filter(brand=self.request.user.customuser.brand)


class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)

    def create(self, request):
        try:
            user = User(username=request.POST["username"])
            user.save()
            user.set_password(request.POST["password"])
            user.save()
            brand = Brand.objects.get(pk=request.POST["brand"])
            cusUser = CustomUser(user=user, brand=brand)
            cusUser.save()
            content = {'User properly created'}
            return Response(content, status=status.HTTP_201_CREATED)
        except:
            content = {"Error user can't be created"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
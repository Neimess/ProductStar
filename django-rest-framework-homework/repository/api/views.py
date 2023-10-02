from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import ApiUser, Repository, Item, Order
from api.serializers import UserSerializer, RepositorySerializer, \
    ItemSerializer, OrderSerializer
from .permissions import IsSupplierPermission, IsConsumerPermission
# Create your views here.


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ["post", "get"]
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []


class RepositoryModelViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    http_method_names = ["post", "get"]
    permission_classes = [IsSupplierPermission]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Создаем объект Item на основе сериализованных данных
            item = serializer.save()

            # Возвращаем созданный объект в ответе
            return Response({
                "message": "Repository created successfully",
                "repository": RepositorySerializer(item).data},
                status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def items(self, request, pk=None):
        repository = get_object_or_404(Repository.objects.all(), id=pk)
        free_items = repository.items
        return Response(
            ItemSerializer(free_items, many=True).data
        )


class ItemModelViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ["post", "get"]
    permission_classes = [IsSupplierPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Создаем объект Item на основе сериализованных данных
            item = serializer.save()

            # Возвращаем созданный объект в ответе
            return Response({"message": "Item created successfully",
                             "item": ItemSerializer(item).data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ["post", "get"]
    permission_classes = [IsConsumerPermission]

    def create(self, request):
        item = get_object_or_404(Item.objects.all(),
                                 id=int(request.data.get("item")))
        quantity = int(request.data.get("quantity"))
        if quantity is not None and quantity <= item.quantity:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                item.quantity -= quantity
                item.save()
                order = serializer.save()
                return Response({
                    "message": "Order created successfully",
                    "order": OrderSerializer(order).data,
                    "item": ItemSerializer(item).data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "message": "Количество получаемого товара " +
                "не может больше, чем есть на складе"
            }, status=status.HTTP_400_BAD_REQUEST)

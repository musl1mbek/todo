from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # http_method_names = ['get', 'post']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


    @action(detail=False, methods=['post'])
    def filter_task(self, request):
        try:
            tick = request.POST['tick']
            if tick:
                t = self.queryset.filter(tick=True)
                query = self.serializer_class(t, many=True)
            else:
                t = self.queryset.filter(tick=False)
                query = self.serializer_class(t, many=True)
            return Response(query.data)
        except Exception as err:
            return Response(f'{err}')

    # def create(self, request):
    #     name = request.POST['name']
    #     text = request.POST['text']
    #     quantity = int(request.POST['quantity'])
    #     price = int(request.POST['price'])
    #     a = Task.objects.create(name=name, text=text, quantity=quantity, price=price)
    #     cash = Cash.objects.first()
    #     cash.money += quantity * price
    #     cash.save()
    #     ser = self.serializer_class(a)
    #     return Response(ser.data)
    #
    # def list(self, request):
    #     try:
    #         a = 'sardor'
    #         b = self.queryset.filter(name__icontains=a)
    #         ser = self.serializer_class(b, many=True)
    #         return Response(ser.data)
    #     except Exception as err:
    #         return Response(f'{err}')

    # def perform_update(self, request):
    #     try:
    #         print("asdasdasdasd")
    #         return Response("asjkdhjkasd")
    #     except Exception as err:
    #         print(f'{err}')
    #         return Response(f'{err}')
    #
    #
    # def partial_update(self, request, *args, **kwargs):
    #     try:
    #         pass
    #         return Response('asdasd')
    #     except Exception as err:
    #         return Response('asdasd')
    #

    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         print("smth")
    #         return Response('smth')
    #     except Exception as err:
    #         return Response("fghjk")


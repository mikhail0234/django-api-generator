from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializers import ProductSerializer
from app.models import Product


class ProductAPIView(APIView):

    def get(self, request, id):
        try:
            item = Product.objects.get(pk=id)
            serializer = ProductSerializer(item)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=404)

    def put(self, request, id):
        try:
            item = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return Response(status=404)
        serializer = ProductSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        try:
            item = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProductAPIListView(APIView):

    def get(self, request,):
        items = Product.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

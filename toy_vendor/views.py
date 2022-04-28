from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from toy_vendor.models import Toy
from toy_vendor.serializers import ToySerializer

class Listar(APIView):
    
    def get(self, request):
        
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return Response(toys_serializer.data, status=status.HTTP_302_FOUND)

    def post(self, request):
        serializer = ToySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response(data=request.data.get('name'))


class Detail(APIView):

    def number_toy(self, pk_):
        try :
            self.toy = Toy.objects.get(pk=pk_)
            return True
        except Toy.DoesNotExist:
            return False

    def get(self, request):
        if self.number_toy(request.data.get('pk')):
            return Response(ToySerializer(self.toy).data, status=status.HTTP_302_FOUND)
        else:
            return Response({'Found':False},status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request):
        if self.number_toy(request.data.get('pk')):
            serializer = ToySerializer(self.toy, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Found':False},status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        if self.number_toy(request.data.get('pk')):
            self.toy.delete()            
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Found':False},status=status.HTTP_404_NOT_FOUND)

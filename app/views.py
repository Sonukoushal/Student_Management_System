from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentView(APIView):
    def get(self,request):
     try:
        object=Student.objects.all()
        serializer=StudentSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
     except:
        return Response({"error":"get function not work"},status=status.HTTP_400_BAD_REQUEST)
     
class StudentAdd(APIView):
   def post(self,request):
      is_many = isinstance(request.data, list)
      serializer=StudentSerializer(data=request.data,many=is_many)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
class GetOne(APIView):
   def get(self,request,id):
      try: 
        object=Student.objects.get(id=id)
        serializer=StudentSerializer(object)
        return Response(serializer.data,status=status.HTTP_200_OK)
      except Student.DoesNotExist:
         return Response({"error":"object not found"},status=status.HTTP_404_NOT_FOUND)
      
class Update(APIView):
   def put(self,request,id):
      try:
         object=Student.objects.get(id=id)
      except Student.DoesNotExist:
         return Response({"error":"object not found"},status=status.HTTP_404_NOT_FOUND)
      serializer=StudentSerializer(object,data=request.data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_)
   
class studentpatch(APIView):
   def patch(self,request,id):
     try:
        object=Student.objects.get(id=id)
     except Student.DoesNotExist:
        return Response({"error":"object not found"},status=status.HTTP_404_NOT_FOUND)
     serializer=StudentSerializer(object,data=request.data,partial=True)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
class StudentDelete(APIView):
   def delete(self,request,id):
      try:
         object=Student.objects.get(id=id)
         object.delete()
         return Response({"success":"object delete successfully"},status=status.HTTP_204_NO_CONTENT)
      except Student.DoesNotExist:
         return Response({"error":"object not found"},status=status.HTTP_404_NOT_FOUND)
      
         
      


    

        


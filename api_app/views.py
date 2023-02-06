from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE',])  # allowing different kinds of requests that our api will receive only
def checking_api(request):
    """In this I am receiving different requests like  GET, POST, PUT or DELETE to just check everything is working fine
       and I receving the parse content using request.data or we can also use request.body which not parsed. So 
       It's better to use request.data ok
    """
    
    # receiving get requests with request.data
    if request.method == 'GET':
        # here we can our custom logic to handle that request
        json_data = request.data
        res = {'response': 'GET request is received', "data is ": json_data,}
        return Response(res)
    
    # here receiving post request with data using request.data
    if request.method == 'POST':
        # here we can our custom logic to save or other logic

        json_data = request.data 
        print('\n post request is received\n', json_data)
        return JsonResponse(json_data)
    
    if request.method == 'PUT':  # request use for complete update
        json_data = request.data
        res  = {'Response': 'PUT  request is received'}
        return Response(res)
    
    # receiving delete request 
    if request.method == 'DELETE':
        json_data = request.data # data from request.data or request.body parsed ok
        res = {'request': "Delete request is received", 'data': json_data}
        print('Delete request is received', json_data)
        return Response(res)


# here I am building api using function-based view of rest_framework

@api_view(['GET','POST', 'PATCH', 'DELETE']) # define that only this request will going to process rest are consider as 405 error
def student_api(request):
    """This endpoint/function will provide functionaly of
        read data, inserted data,update and delete operation can be performed
        using this function.
    If having any suggestion/query than email me krishnayadav78887@gmail.com.
    Thank You

    
    Krishna yadav
    """

    def except_errr(status = status.HTTP_404_NOT_FOUND):
        """default exception handling here. 
           I am returning status as 404_not_found error ok
        """
        return Response(status=status)
    
    # receiving GET request here
    if request.method == 'GET':
        python_data = request.data 

        id  = python_data.get('id', None) # getting id if passed 

        if id is not None: # checking weather Id is exists
            try:
                stu = Student.objects.get(pk = id)
            except Student.DoesNotExist:
                return except_errr()
            else:
                serializer = StudentSerializer(stu)
                return Response(serializer.data, status =status.HTTP_200_OK )
        else:
            all_stus = Student.objects.all()
            serializer = StudentSerializer(all_stus, many=True)
            return Response(serializer.data, status =status.HTTP_200_OK)
    
    # receiving post request here
    if request.method == 'POST':
        print('\n post request is received\n')
        python_data = request.data # receiving request.data here

        # serializing the data here
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():  # checking serializer is valid or not
            serializer.save()      # saving data/
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # returning here serializers errors
            return Response(serializer.errors)
            
    # receving PATCH request for partial update
    if request.method == 'PATCH':
        python_data = request.data 
        id  = python_data.get('id', None)

        if id is not None:
            try:
                stu = Student.objects.get(pk=id)
            except Student.DoesNotExist: 
                return except_errr()
            else:
                serializer = StudentSerializer(stu, data=python_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors)

        else:
            return except_errr()
     
     # delete request here
    if request.method == 'DELETE':
        python_data = request.data 
        id = python_data.get('id', None)

        if id is not None:
            try:
                stu  = Student.objects.get(pk = id)
            except Student.DoesNotExist:
                return except_errr()
            else:
                stu.delete()
                res = {'deleted': 'Student deleted successfuly'}
                return Response(res, status = status.HTTP_200_OK)
        else:
            return except_errr()
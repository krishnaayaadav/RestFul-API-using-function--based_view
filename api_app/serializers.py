

# This file contains our serailizers that we use to create api-s


from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model  =  Student
        fields =  ('stu_id','name', 'email', 'age')
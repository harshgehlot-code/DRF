from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    # Defining the fields that will be serialized
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


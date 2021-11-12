from rest_framework import serializers
from .models import Lookup

class LookupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lookup
        fields = '__all__'





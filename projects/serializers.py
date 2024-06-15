from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title', 'description', 'tecnology', 'created_at')
        #Campo solo para leer no va a poder actualizarse
        read_only_fields = ('created_at',)
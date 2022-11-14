from rest_framework import serializers

from npo_project.models import Program, ProgramCharacteristic


class ProgramCharacteristicSerializer(serializers.ModelSerializer):
    program = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name'
    )

    class Meta:
        model = ProgramCharacteristic
        fields = ('id', 'text', 'program')


class ProgramSerializer(serializers.ModelSerializer):
    characteristics = ProgramCharacteristicSerializer(
        read_only=True, many=True
    )

    class Meta:
        model = Program
        fields = ('id', 'name', 'image', 'description', 'location',
                  'characteristics')

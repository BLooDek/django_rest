from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'

    def create(self, validated_data):
        author = self.context['request'].user
        note = Note.objects.create(**validated_data, author=author)
        note.author = author
        print(note)
        return note

        # print(self.context.get('user'))
        # return self.context.get('user')
# def create(self, validated_data):
#     profile_data = validated_data.pop('profile')
#     user = User.objects.create_user(**validated_data)
#     UserProfile.objects.create(
#         user = user,
#         first_name = profile_data['first_name'],
#         last_name= profile_data['last_name'],
#                  )
#     return user
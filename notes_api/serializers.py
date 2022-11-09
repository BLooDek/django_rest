from requests import Response
from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


    # answer, created = Answer.objects.get_or_create(
    #     question=validated_data.get('question', None),
    #     defaults={'answer': validated_data.get('answer', None)})

    # return answer

    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.body = validated_data.get('body', instance.body)
    #     instance.is_published = validated_data.get('is_published', instance.is_published)
    #     return instance

    # title = models.CharField(max_length=200)
    # body = models.TextField(default="", null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # is_published = models.BooleanField(default=True)
    # author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, unique=False)

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

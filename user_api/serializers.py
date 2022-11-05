from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.serializers import ModelSerializer
from user_api.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ('username','email', 'last_login', 'date_joined', 'is_staff')
        fields = '__all__'


class CustomRegisterSerializer(RegisterSerializer):
    """Use default serializer except don't user username"""

    username = None

    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser, Department

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    firstname = serializers.CharField() 
    lastname = serializers.CharField() 
    email = serializers.EmailField()
    phone = serializers.CharField()
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict["firstname"] = self.validated_data.get("firstname")
        data_dict["lastname"] = self.validated_data.get("lastname")
        data_dict["email"] = self.validated_data.get("email")
        data_dict["phone"] = self.validated_data.get("phone")
        data_dict["department"] = self.validated_data.get("department")
        return data_dict

    # def custom_signup(self, request, user):
    #     user.firstname = self.validated_data.get("firstname")
    #     user.lastname = self.validated_data.get("lastname")
    #     user.email = self.validated_data.get("email")
    #     user.phone = self.validated_data.get("phone")
    #     user.department = self.validated_data.get("department")
    #     user.save(update_fields=["firstname", "lastname", "email", "phone", "department"])

    def create(self, validated_data):
        firstname = validated_data.pop("firstname")
        lastname = validated_data.pop("lastname")
        username = f"{firstname[0].lower()}{lastname.lower()}"
        validated_data["username"] = username

        department_id = validated_data.pop("department")
        validated_data["department"] = department_id

        user = CustomUser.objects.create_user(**validated_data)
        return user

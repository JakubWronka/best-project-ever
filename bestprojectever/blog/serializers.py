from rest_framework import serializers
from .models import CustomUser, CustomUserProfile, Article

class CustomUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserProfile
        fields = ['date_of_birth', 'country', 'city', 'bio', 'photo']

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    profile = CustomUserProfileSerializer(required=True)
    class Meta:
        model = CustomUser
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        CustomUserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.date_of_birth = profile_data.get('date_of_birth', profile.date_of_birth)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance

class ArticleSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    # By default, only primary key of an author will be displayed - by that we display all the fields that are included in CustomUserSerializer
    class Meta:
        model = Article
        fields = '__all__'
        # When all fields from the model are meant to be used, we don't need to specify them one by one, but instead just use '__all__' to get all fields

from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

class UserSerializer(UserDetailsSerializer):

    nick_name = serializers.CharField(source="UserProfile.nick_name")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('nick_name',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        nick_name = profile_data.get('nick_name')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data and nick_name:
            profile.nick_name = nick_name
            profile.save()
        return instance

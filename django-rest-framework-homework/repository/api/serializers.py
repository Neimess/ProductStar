from rest_framework import serializers
from rest_framework import validators
from api.models import ApiUser, Repository, Item, Order


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(ApiUser.objects.all())])
    password = serializers.CharField(
        min_length=8, max_length=20, write_only=True)
    user_type = serializers.ChoiceField(choices=ApiUser.USER_TYPES)

    def update(self, instance: ApiUser, validated_data):
        if email := validated_data.get("email"):
            instance.email = email
            instance.save(update_fields=["email"])

        if password := validated_data.get("password"):
            instance.set_password(password)
            instance.save(update_fields=["password"])
        return instance

    def create(self, validated_data):
        user = ApiUser.objects.create(
            email=validated_data.get("email"),
            user_type=validated_data.get("user_type"),
        )
        user.set_password(validated_data.get("password"))
        user.save(update_fields=["password"])

        return user


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

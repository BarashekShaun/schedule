import django_filters
from django_filters import OrderingFilter, DateFromToRangeFilter, CharFilter
from rest_framework import serializers
from .models import Event, AdvUser, Organization


class EventFilter(django_filters.FilterSet):
    date = DateFromToRangeFilter()
    title = CharFilter(lookup_expr='icontains')
    ordering = OrderingFilter(fields=('date', 'date'))

    class Meta:
        model = Event
        fields = ['title']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['title', 'postcode', 'address']

    def to_representation(self, instance):
        return {
            "title": instance.title,
            "address": f"{instance.postcode} {instance.address}"
        }


class UserSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = AdvUser
        fields = ['username', 'organization']


class EventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=250)
    organizations = UserSerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)
    date = serializers.DateTimeField()
    organization_key = serializers.CharField(write_only=True)

    def create(self, validated_data):
        organization_key = validated_data.pop('organization_key')
        new_event = Event.objects.create(**validated_data)
        keys = [int(key) for key in organization_key.split(', ')]
        new_event.organizations.add(*keys)
        return new_event

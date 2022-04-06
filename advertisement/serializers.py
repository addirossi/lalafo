from rest_framework import serializers

from .models import Advertisement, AdvertisementGallery


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementGallery
        fields = ['picture']


class CreateAdSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        write_only=True,
        child=serializers.ImageField()
    )

    class Meta:
        model = Advertisement
        fields = '__all__'

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        ad = super().create(validated_data)
        for picture in images:
            AdvertisementGallery.objects.create(advertisement=ad,
                                                picture=picture)
        return ad


class AdvertisementListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'city', 'price', 'image']

    def get_image(self, advertisement):
        first_image_obj = advertisement.images.first()
        if first_image_obj is not None:
            return first_image_obj.picture.url
        return ''

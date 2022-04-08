from rest_framework import serializers

from .models import Advertisement, AdvertisementGallery, Category


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementGallery
        fields = ['picture']


# class CreateAdSerializer(serializers.ModelSerializer):
#     images = serializers.ListField(
#         write_only=True,
#         child=serializers.ImageField()
#     )
#
#     class Meta:
#         model = Advertisement
#         # fields = '__all__'
#         exclude = ['author']
#
#     def create(self, validated_data):
#         validated_data['author'] = self.context['request'].user
#         images = validated_data.pop('images', [])
#         ad = super().create(validated_data)
#         for picture in images:
#             AdvertisementGallery.objects.create(advertisement=ad,
#                                                 picture=picture)
#         return ad
#

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


# class AdvertisementDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Advertisement
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['images'] = ImageSerializer(instance.images.all(),
#                                                    many=True).data
#         return representation


# class UpdateAdvertisementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Advertisement
#         fields = ['title', 'text', 'city', 'price']


class AdvertisementSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        write_only=True,
        child=serializers.ImageField()
    )

    class Meta:
        model = Advertisement
        # fields = '__all__'
        exclude = ['author']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        images = validated_data.pop('images', [])
        ad = super().create(validated_data)
        for picture in images:
            AdvertisementGallery.objects.create(advertisement=ad,
                                                picture=picture)
        return ad

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(),
                                                   many=True).data
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

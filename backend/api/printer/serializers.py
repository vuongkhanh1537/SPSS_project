from rest_framework import serializers

from .models import ModelPrinter, Feature, OrderPrinter



class FeatureSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Feature
        fields = [
            'id',
            'model',
            'feature'
        ]
        read_only_fields = ('model',)

class ModelPrinterSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)

    class Meta:
        model = ModelPrinter
        fields = [
            "id",
            "model",
            "created_by",
            "features",
        ]

    def create(self, validated_data):
        features = validated_data.pop('features')
        model = ModelPrinter.objects.create(**validated_data)
        for feature in features:
            Feature.objects.create(**feature, model=model)
        return model

    def update(self, instance, validated_data):
        features = validated_data.pop('features')
        instance.model = validated_data.get("model", instance.model)
        instance.save()
        keep_features = []
        for feature in features:
            if "id" in feature.keys():
                if Feature.objects.filter(id=feature["id"]).exists():
                    c = Feature.objects.get(id=feature["id"])
                    c.feature = feature.get('feature', c.feature)
                    c.save()
                    keep_features.append(c.id)
                else:
                    continue
            else:
                c = Feature.objects.create(**feature, model=instance)
                keep_features.append(c.id)

        for feature in instance.features:
            if feature.id not in keep_features:
                feature.delete()

        return instance

class PrinterSerializer(serializers.ModelSerializer):
    pass

class PrinterSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = serializers.CharField()
    created_at = serializers.DateTimeField()
class OrderPrinterSerializer(serializers.Serializer):
    class Meta:
        model = OrderPrinter
        fields = '__all__'
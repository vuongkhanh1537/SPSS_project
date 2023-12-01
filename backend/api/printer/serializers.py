from rest_framework import serializers

from .models import ModelPrinter, Feature, OrderPrinter, Printer, Floor, Building, Institution, PrinterViews


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
class BuildingSerializer(serializers.ModelSerializer):
    inst = serializers.ChoiceField(choices=Institution.choices)

    class Meta:
        model = Building
        fields = '__all__'

class FloorSerializer(serializers.ModelSerializer):
    building_code = serializers.SerializerMethodField()

    class Meta:
        model = Floor
        fields = '__all__'

    def get_building_code(self, obj):
        return BuildingSerializer(obj.building_code).data


class PrinterSerializer(serializers.ModelSerializer):
    floor = serializers.SerializerMethodField()
    
    def get_floor(self, obj):
        return obj.floor.floor_code
    class Meta:
        model = Printer
        fields = '__all__'

class PrinterMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = ["status"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data = serializers.ModelSerializer.to_representation(self, instance)
        return data


class CreatePrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        exclude = ("updated_at",)


class PrinterDetailSerializer(serializers.ModelSerializer):
    model = serializers.SerializerMethodField()
    floor = serializers.SerializerMethodField()

    def get_floor(self, obj):
        return obj.floor.floor_code

    class Meta:
        model = Printer
        exclude = "updated_at"


class PrinterViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterViews
        exclude = "updated_at"

class OrderPrinterSerializer(serializers.Serializer):
    class Meta:
        model = OrderPrinter
        fields = '__all__'
        read_only_fields = ('ink_status', 'model')
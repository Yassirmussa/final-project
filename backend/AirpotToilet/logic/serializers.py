from rest_framework import serializers
from logic.models import Staff, Day, Allocation, Feedback

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class FeedbackSerializer(serializers.ModelField):
    class Meta:
        model = Feedback
        fields = '__all__'

class AllocationSerializer(serializers.ModelSerializer):
    Sid = StaffSerializer(source='Sid', read_only=True)
    Did = DaySerializer(source='Did', read_only=True)
    class Meta:
        model = Allocation
        fields = '__all__'


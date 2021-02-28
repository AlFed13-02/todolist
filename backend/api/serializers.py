import datetime

from django.utils import timezone
from django.conf import settings
from rest_framework imoprt serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'owner',
            'to_do',
            'date',
            'time',
            'done'
        ]

    def validate_date(self, value):
        '''Checks the value for belonging to the past.'''
        if value < timezone.localdate():
            raise serializers.ValidationError()
        return value

    def validate_time(self, value):
        '''Checks the value for belonging to the past.'''
        tz = timezone.get_current_timezone()
        date = self.initial_data['date']
        date = datetime.date.fromisoformat(date)
        date = datetime.datetime.combine(date, value, tzinfo=tz)
        if date <= timezone.now:
            raise serializers.ValidationError
        return value


    class UserSerializer(serializers.ModelSerializer):
        tasks = seiralizers.PrimaryKeyRelatedField(
            many=True,
            queryset=Task.objects.all()
        )
        
        class Meta:
            model = settings.AUTH_USER_MODEL
            fields = [
                'user_name',
                'first_name',
                'last_name',
                'tasks',
            ]
                
        

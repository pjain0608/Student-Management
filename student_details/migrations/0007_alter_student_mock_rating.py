# Generated by Django 5.1.3 on 2024-12-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_details', '0006_alter_student_mock_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Mock_Rating',
            field=models.CharField(default='0', max_length=10),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_details', '0004_alter_student_age_alter_student_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='Mock_Rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='YOP',
            field=models.IntegerField(),
        ),
    ]
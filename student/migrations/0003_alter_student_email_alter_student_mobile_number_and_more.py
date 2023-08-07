# Generated by Django 4.2.3 on 2023-08-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_created_at_alter_student_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(unique=True),
        ),
    ]

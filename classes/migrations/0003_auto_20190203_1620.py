# Generated by Django 2.0.6 on 2019-02-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20190203_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='exam_grade',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
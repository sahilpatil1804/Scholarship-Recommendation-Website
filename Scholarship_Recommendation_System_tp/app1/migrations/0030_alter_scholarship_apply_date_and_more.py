# Generated by Django 4.1.2 on 2022-11-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='apply_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='degree',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='eligibility',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='image_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='link',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholarship_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='subject',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='tution_structure',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='university_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
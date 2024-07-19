# Generated by Django 4.1.2 on 2022-10-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_delete_user_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarships',
            name='Nationality',
        ),
        migrations.RemoveField(
            model_name='scholarships',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='scholarships',
            name='University',
        ),
        migrations.AddField(
            model_name='scholarships',
            name='Eligibility',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='Image_link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='Scholarship_details',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='Subject',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='Tution_structure',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='University_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='Apply_date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='Country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='Degree',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='Link',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='Title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
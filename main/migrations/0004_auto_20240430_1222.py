# Generated by Django 3.1.1 on 2024-04-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_doctoradd_doctor_join_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hosptal_name', models.CharField(max_length=255)),
                ('Image', models.FileField(upload_to='hospitel_image')),
                ('Area', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=26)),
                ('Symptoms', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor_consultation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='doctoradd',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
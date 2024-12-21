# Generated by Django 5.0.6 on 2024-05-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('current_location', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='dump_images/')),
                ('current_city', models.CharField(max_length=100)),
                ('dump_type', models.CharField(choices=[('Sukha', 'Sukha'), ('Gilla', 'Gilla')], max_length=20)),
                ('dump_size', models.CharField(choices=[('Small', 'Small'), ('Normal', 'Normal'), ('Large', 'Large')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demotable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('file', models.FileField(upload_to='files/')),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('is_active', models.BooleanField(default=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NS', 'Not Specified')], max_length=2)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='upload',
            options={},
        ),
    ]

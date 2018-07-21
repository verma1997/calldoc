# Generated by Django 2.0.7 on 2018-07-20 12:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0006_auto_20180717_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('address', models.TextField(blank=True, max_length=5000, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('rating', models.PositiveSmallIntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='hospital.Hospital')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specialisation',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'specialisation',
                'verbose_name_plural': 'specialisations',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialisation',
            field=models.ManyToManyField(related_name='speciality', to='hospital.Specialisation'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hospital',
            name='specialisation',
            field=models.ManyToManyField(related_name='speciality_of_hospital', to='hospital.Specialisation'),
        ),
    ]

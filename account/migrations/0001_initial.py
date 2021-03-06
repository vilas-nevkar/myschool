# Generated by Django 3.0.8 on 2020-07-18 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=128)),
                ('role', models.CharField(blank=True, choices=[('headmaster', 'Headmaster'), ('teacher', 'Teacher'), ('non_teacher', 'Non Teacher')], max_length=128)),
                ('dob', models.DateField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10)),
                ('photo', models.ImageField(blank=True, upload_to='account/staff/')),
                ('uid', models.CharField(blank=True, max_length=12)),
                ('cast', models.CharField(blank=True, max_length=512)),
                ('is_teacher', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.Address')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.CastCategory')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.Language')),
                ('religion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.Religion')),
                ('standard', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.Standard')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

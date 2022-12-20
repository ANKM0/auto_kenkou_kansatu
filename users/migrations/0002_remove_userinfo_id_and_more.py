# Generated by Django 4.1.4 on 2022-12-20 02:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_info_created_at',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_info_updated_at',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_info_class_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='クラス番号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_info_student_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(40)], verbose_name='出席番号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
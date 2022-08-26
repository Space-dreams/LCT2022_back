# Generated by Django 3.2.13 on 2022-08-26 09:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nick_name', models.CharField(blank=True, max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Аватар')),
                ('telephone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'профиль',
                'verbose_name_plural': 'профили пользователей',
            },
            managers=[
                ('objects', main_app.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Направление проекта')),
            ],
            options={
                'verbose_name': 'направление проекта',
                'verbose_name_plural': 'направления проектов',
            },
        ),
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.PositiveIntegerField(choices=[(1, 'Open'), (2, 'Close')], default=1, verbose_name='Доступность проекта')),
            ],
            options={
                'verbose_name': 'доступность проекта',
                'verbose_name_plural': 'доступность проекта',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.PositiveIntegerField(choices=[(1, 'Tarif 1'), (2, 'Tarif 2'), (3, 'Tarif 3')], default=1, verbose_name='Тариф')),
            ],
            options={
                'verbose_name': 'тариф',
                'verbose_name_plural': 'тарифы',
            },
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Стек технологий')),
            ],
            options={
                'verbose_name': 'стек технологий',
                'verbose_name_plural': 'стек технологий',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.JSONField()),
            ],
            options={
                'verbose_name': 'стадия проекта',
                'verbose_name_plural': 'стадии проектов',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Phisical'), (2, 'Legal')], default=1, verbose_name='Статус - физическое/юридическое лицо')),
            ],
            options={
                'verbose_name': 'статус',
                'verbose_name_plural': 'статусы',
            },
        ),
        migrations.CreateModel(
            name='TypeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveIntegerField(choices=[(1, 'Commercial'), (2, 'Non commercial')], default=1, verbose_name='Тип проекта - коммерческий/некоммерческий')),
            ],
            options={
                'verbose_name': 'тип проекта',
                'verbose_name_plural': 'типы проектов',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название проекта')),
                ('members_limit', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Максимальное количество участников')),
                ('deadline', models.DateField(verbose_name='Срок окончания проекта')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Рейтинг')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.direction', verbose_name='Направление проекта')),
                ('id_project_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.typeproject', verbose_name='Тип проекта')),
                ('id_rate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.rate', verbose_name='Тариф')),
                ('id_stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.stage', verbose_name='Стадия проекта')),
                ('id_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.public', verbose_name='Доступность проекта')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Список участников')),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='id_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.status', verbose_name='ID статуса'),
        ),
        migrations.AddField(
            model_name='profile',
            name='stack',
            field=models.ManyToManyField(to='main_app.Stack', verbose_name='Стек технологий'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]

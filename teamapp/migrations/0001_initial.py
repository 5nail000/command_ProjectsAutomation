# Generated by Django 4.2.6 on 2023-10-25 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreeTimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(db_index=True, verbose_name='Слот свободного времени')),
                ('count', models.IntegerField(default=0, verbose_name='Количество слотов')),
                ('week', models.IntegerField(verbose_name='Номер недели')),
            ],
            options={
                'verbose_name': 'Слот свободного времени',
                'verbose_name_plural': 'Слоты свободных времен',
                'ordering': ['count'],
            },
        ),
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('start_time', models.TimeField(verbose_name='Время начала рабочего дня')),
                ('end_time', models.TimeField(verbose_name='Время конца рабочего дня')),
                ('telegram', models.CharField(blank=True, max_length=70, verbose_name='Телеграм')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Уровень ученика')),
            ],
            options={
                'verbose_name': 'Уровень знания',
                'verbose_name_plural': 'Уровни знаний',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('mail', models.CharField(max_length=70, verbose_name='Электронная почта')),
                ('telegram', models.CharField(blank=True, max_length=70, verbose_name='Телеграм')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranks', to='teamapp.rank', verbose_name='Уровень ученика')),
                ('time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='times', to='teamapp.freetimetable', verbose_name='Время созванивания в проекте')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('login', models.CharField(max_length=20, verbose_name='Логин')),
                ('password', models.CharField(max_length=20, verbose_name='Пароль')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='students', serialize=False, to='teamapp.student', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_full', models.BooleanField(default=False, verbose_name='Полная команда')),
                ('first_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_students', to='teamapp.student', verbose_name='Первый ученик')),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managers', to='teamapp.projectmanager', verbose_name='Менеджер')),
                ('second_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_students', to='teamapp.student', verbose_name='Второй ученик')),
                ('third_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_students', to='teamapp.student', verbose_name='Третий ученик')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.freetimetable', verbose_name='Время созванивания')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sent', models.BooleanField(default=False, verbose_name='Отправлено')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invite_students', to='teamapp.student', verbose_name='Ученик')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='teamapp.team', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Приглашение',
                'verbose_name_plural': 'Приглашения',
            },
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-16 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_quiz_ended'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.category'),
        ),
    ]

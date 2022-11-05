# Generated by Django 3.2.16 on 2022-11-05 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_alter_curator_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direction', to='lms.curator')),
            ],
        ),
    ]
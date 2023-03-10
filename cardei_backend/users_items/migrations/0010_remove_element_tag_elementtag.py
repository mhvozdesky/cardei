# Generated by Django 4.1 on 2023-01-23 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_items', '0009_alter_tag_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='tag',
        ),
        migrations.CreateModel(
            name='ElementTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='element_tag', to='users_items.element')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='element_tag', to='users_items.tag')),
            ],
        ),
    ]

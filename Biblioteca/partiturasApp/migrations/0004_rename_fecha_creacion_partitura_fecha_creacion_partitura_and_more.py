# Generated by Django 5.2.4 on 2025-07-25 23:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("partiturasApp", "0003_alter_partitura_compositor_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="partitura",
            old_name="fecha_creacion",
            new_name="fecha_creacion_partitura",
        ),
        migrations.AddField(
            model_name="compositor",
            name="fecha_ingreso",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="instrumento",
            name="fecha_ingreso",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="partitura",
            name="fecha_ingreso",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]

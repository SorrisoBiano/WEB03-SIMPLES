# Generated by Django 5.1.3 on 2024-11-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_crianca_filial_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filial",
            name="nome_filial",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

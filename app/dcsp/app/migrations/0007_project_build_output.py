# Generated by Django 4.2.6 on 2024-01-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_project_last_built_project_last_modified"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="build_output",
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
# Generated by Django 4.2.6 on 2024-01-17 07:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_userprojectattribute_repo_password_token_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="external_repo_password_token",
        ),
        migrations.RemoveField(
            model_name="project",
            name="external_repo_username",
        ),
    ]

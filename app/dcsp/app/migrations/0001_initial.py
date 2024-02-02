# Generated by Django 4.2.6 on 2024-01-08 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "external_repo_url",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "external_repo_username",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "external_repo_password_token",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "member",
                    models.ManyToManyField(
                        blank=True,
                        related_name="member_many_to_many",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner_foreign_key",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="owner",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="UserProjectAttribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_accessed", models.DateTimeField(auto_now=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.project"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "project")},
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "default_github_username",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "default_github_host",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "github_token",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "member",
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
                ),
                (
                    "project_access",
                    models.ManyToManyField(blank=True, to="app.project"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="user_interaction",
            field=models.ManyToManyField(
                blank=True,
                related_name="last_updated_by_user_many_to_many",
                through="app.UserProjectAttribute",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
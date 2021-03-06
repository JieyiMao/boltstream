# Generated by Django 2.2 on 2019-04-29 18:08

import functools
import uuid

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.crypto
import django.utils.timezone
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models

import boltstream.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0011_update_proxy_permissions")]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"swappable": "AUTH_USER_MODEL"},
            managers=[("objects", boltstream.models.UserManager())],
        ),
        migrations.CreateModel(
            name="Feed",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stream",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        default=functools.partial(
                            django.utils.crypto.get_random_string, *(20,), **{}
                        ),
                        editable=False,
                        max_length=20,
                        unique=True,
                        verbose_name="Stream key",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "ingest_host",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created"
                    ),
                ),
                (
                    "started_at",
                    models.DateTimeField(blank=True, null=True, verbose_name="Started"),
                ),
                (
                    "program_date_time",
                    models.DateTimeField(
                        blank=True,
                        help_text="The original #EXT-X-PROGRAM-DATE-TIME from the HLS manifest used to calculate synchronization offsets.",
                        null=True,
                        verbose_name="Program Date Time",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                ("credits_used", models.PositiveIntegerField(default=0)),
                (
                    "acrcloud_acr_id",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=100,
                        null=True,
                        verbose_name="ACRCloud ACR ID",
                    ),
                ),
                (
                    "feeds",
                    models.ManyToManyField(
                        related_name="streams", to="boltstream.Feed"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="streams",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ("created_at",)},
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                ("starts_at", models.DateTimeField(db_index=True)),
                ("ends_at", models.DateTimeField(db_index=True)),
                ("payload", jsonfield.fields.JSONField(blank=True)),
                (
                    "feed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="boltstream.Feed",
                    ),
                ),
            ],
            options={"ordering": ("starts_at", "ends_at")},
        ),
        migrations.CreateModel(
            name="Viewer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_viewed_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "stream",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="viewers",
                        to="boltstream.Stream",
                    ),
                ),
                (
                    "viewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="viewing_streams",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("viewer", "stream")}},
        ),
        migrations.CreateModel(
            name="Credit",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                ("amount", models.PositiveIntegerField(default=0)),
                (
                    "stream",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credits",
                        to="boltstream.Stream",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credits",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("user", "stream")}},
        ),
    ]

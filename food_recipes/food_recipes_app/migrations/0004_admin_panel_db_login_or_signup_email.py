# Generated by Django 5.0.1 on 2024-02-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_recipes_app', '0003_admin_panel_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_panel_db',
            name='login_or_signup_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]

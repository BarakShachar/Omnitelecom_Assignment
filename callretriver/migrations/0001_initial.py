# Generated by Django 4.1.4 on 2022-12-29 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_child', to='callretriver.company')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_team_child', to='callretriver.company')),
                ('team_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_child', to='callretriver.team')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_user_child', to='callretriver.company')),
                ('team_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_user_child', to='callretriver.team')),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='call_owner', to='callretriver.user')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-29 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('callretriver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_child', to='callretriver.company'),
        ),
    ]

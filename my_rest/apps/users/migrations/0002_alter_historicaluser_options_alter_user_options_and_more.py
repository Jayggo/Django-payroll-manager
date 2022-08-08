# Generated by Django 4.0.6 on 2022-08-08 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_company_phone_alter_historicalcompany_phone'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaluser',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical User'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='company',
            field=models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='companies.company', verbose_name='company'),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='company'),
        ),
    ]

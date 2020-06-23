# Generated by Django 3.0.5 on 2020-06-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpmate', '0002_auto_20200605_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='civil_note',
            name='is_semester_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_note',
            name='is_semester_3',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_note',
            name='is_semester_4',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_note',
            name='is_semester_5',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_note',
            name='is_semester_6',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_note',
            name='is_semester_7',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_note',
            name='is_semester_8',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_qp',
            name='is_semester_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_qp',
            name='is_semester_3',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_qp',
            name='is_semester_4',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_qp',
            name='is_semester_5',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_qp',
            name='is_semester_6',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_qp',
            name='is_semester_7',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_qp',
            name='is_semester_8',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_note',
            name='is_semester_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_note',
            name='is_semester_3',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_note',
            name='is_semester_4',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_note',
            name='is_semester_5',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_note',
            name='is_semester_6',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_note',
            name='is_semester_7',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_note',
            name='is_semester_8',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_qp',
            name='is_semester_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_qp',
            name='is_semester_3',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_qp',
            name='is_semester_4',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_qp',
            name='is_semester_5',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_qp',
            name='is_semester_6',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_qp',
            name='is_semester_7',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comp_qp',
            name='is_semester_8',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fe_note',
            name='is_semester_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fe_note',
            name='is_semester_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fe_qp',
            name='is_semester_1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fe_qp',
            name='is_semester_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_note',
            name='is_semester_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_note',
            name='is_semester_3',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_note',
            name='is_semester_4',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_note',
            name='is_semester_5',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_note',
            name='is_semester_6',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_note',
            name='is_semester_7',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_note',
            name='is_semester_8',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_qp',
            name='is_semester_2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_qp',
            name='is_semester_3',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_qp',
            name='is_semester_4',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_qp',
            name='is_semester_5',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_qp',
            name='is_semester_6',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_qp',
            name='is_semester_7',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mech_qp',
            name='is_semester_8',
            field=models.BooleanField(default=True),
        ),
    ]

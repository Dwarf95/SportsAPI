# Generated by Django 3.1.2 on 2020-10-02 12:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_socceroffensivestats'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoccerDefensiveStats',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('shots_penalty_shot_allowed', models.IntegerField()),
                ('goals_penalty_shot_allowed', models.IntegerField()),
                ('goals_against_average', models.IntegerField()),
                ('goals_against_total', models.IntegerField()),
                ('saves', models.IntegerField()),
                ('save_percentage', models.FloatField()),
                ('catches_punches', models.IntegerField()),
                ('shots_on_goal_total', models.IntegerField()),
                ('shots_shootout_total', models.IntegerField()),
                ('shots_shootout_allowed', models.IntegerField()),
                ('shots_blocked', models.IntegerField()),
                ('shutouts', models.IntegerField()),
                ('goals_own', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SoccerFoulStats',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fouls_suffered', models.IntegerField()),
                ('fouls_commited', models.IntegerField()),
                ('cautions_total', models.IntegerField()),
                ('cautions_pending', models.IntegerField()),
                ('caution_points_total', models.IntegerField()),
                ('caution_points_pending', models.IntegerField()),
                ('ejections_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SoccerEventStates',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('period_time_elapsed', models.CharField(default='', max_length=250)),
                ('period_time_remaining', models.CharField(default='', max_length=250)),
                ('minutes_elapsed', models.IntegerField()),
                ('period_minute_elapsed', models.IntegerField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.events')),
                ('score_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_team', to='api.teams')),
                ('score_team_away', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_team_away', to='api.teams')),
                ('score_team_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_team_home', to='api.teams')),
                ('score_team_opposing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_team_opposing', to='api.teams')),
            ],
        ),
        migrations.CreateModel(
            name='SoccerActionPlays',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('play_result', models.CharField(default='', max_length=200)),
                ('points', models.FloatField()),
                ('soccer_event_state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.eventstates')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teams')),
            ],
        ),
        migrations.CreateModel(
            name='SoccerActionParticipants',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.persons')),
                ('soccer_action_play_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.socceractionplays')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teams')),
            ],
        ),
    ]

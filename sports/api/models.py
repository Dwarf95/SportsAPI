import uuid

from django.db import models


class Locations(models.Model):
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    area = models.CharField(max_length=250, default='')
    country = models.CharField(max_length=250, default='')
    timezone = models.CharField(max_length=100, default='')
    latitude = models.CharField(max_length=200, default='')
    longitude = models.CharField(max_length=200, default='')
    country_code = models.CharField(max_length=10, default='')


class Sites(models.Model):
    sites_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site_key = models.CharField(max_length=200, default='')
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)


class Addresses(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    language = models.CharField(max_length=200, default='')
    suite = models.IntegerField()
    floor = models.IntegerField()
    building = models.IntegerField()
    street_number = models.IntegerField()
    street_prefix = models.CharField(max_length=50, default='')
    street = models.CharField(max_length=250, default='')
    street_suffix = models.CharField(max_length=50, default='')
    neighborhood = models.CharField(max_length=250, default='')
    district = models.CharField(max_length=250, default='')
    locality = models.CharField(max_length=250, default='')
    county = models.CharField(max_length=250, default='')
    region = models.CharField(max_length=250, default='')
    postal_code = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=250, default='')


class Events(models.Model):
    SITE_ALIGN_CHOICES = (
        ('HOME_TEAM', 'Home Team'),
        ('NEUTRAL', 'Neutral'),
    )
    EVENT_STATUS_CHOICES = (
        ('PRE_EVENT', 'pre-event'),
        ('MID_EVENT', 'mid-event'),
        ('POST_EVENT', 'post-event'),
        ('POSTPONED_EVENT', 'postponed'),
        ('CANCELLED_EVENT', 'cancelled'),
    )
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_key = models.CharField(max_length=250, default='')
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    site = models.ForeignKey(Sites, on_delete=models.CASCADE)
    site_alignment = models.CharField(max_length=50, choices=SITE_ALIGN_CHOICES, default='HOME_TEAM')
    event_status = models.CharField(max_length=50, choices=EVENT_STATUS_CHOICES, default='PRE_EVENT')
    last_update = models.DateTimeField()
    event_number = models.IntegerField()
    round_number = models.IntegerField()
    time_certainty = models.CharField(max_length=250, default='')
    broadcast_listing = models.CharField(max_length=250, default='')
    start_date_time_local = models.DateTimeField()
    series_index = models.IntegerField()


class ParticipantsEvents(models.Model):
    PARTICIPANT_CHOICES = (
        ('TEAM', 'Team'),
        ('PLAYER', 'Player')
    )
    ALIGN_CHOICES = (
        ('HOME_TEAM', 'Home Team'),
        ('GUEST_TEAM', 'Guest Team'),
    )
    SCORE_TYPES = (
        ('GOL','Gol'),
        ('KOS','Kos')
    )
    participant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participant_type = models.CharField(max_length=100, choices=PARTICIPANT_CHOICES, default='TEAM')
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    alignment = models.CharField(max_length=100, choices=ALIGN_CHOICES, default='HOME_TEAM')
    score = models.FloatField()
    event_outcome = models.CharField(max_length=250, default='')
    rank = models.FloatField()
    result_effect = models.CharField(max_length=250, default='')
    score_attempts = models.IntegerField()
    sort_order = models.CharField(max_length=10, default='')
    score_type = models.CharField(max_length=200, choices=SCORE_TYPES, default='GOL')


class Periods(models.Model):
    period_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participant_event_id = models.ForeignKey(ParticipantsEvents, on_delete=models.CASCADE)
    period_value = models.CharField(max_length=200, default='')
    score = models.IntegerField()
    rank = models.IntegerField()
    sub_score_key = models.IntegerField()
    sub_score_type = models.CharField(max_length=200, default='')
    sub_score_name = models.CharField(max_length=200, default='')


class Affiliations(models.Model):
    affiliation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    affiliation_type = models.CharField(max_length=200, default='')


class Teams(models.Model):
    team_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_key = models.CharField(max_length=100, default='')
    home_site_id = models.ForeignKey(Sites, on_delete=models.CASCADE)


class AffiliationEvents(models.Model):
    affiliation_events_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    affiliation = models.ForeignKey(Affiliations, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)


class WeatherConditions(models.Model):
    TEMP_UNIT_CHOICES = (
        ('C','Celsius'),
        ('F','Fahrenheit')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    temperature = models.FloatField()
    temperature_unit = models.CharField(max_length=30, choices=TEMP_UNIT_CHOICES, default='C')
    humidity = models.FloatField()
    clouds = models.BooleanField()
    wind_direction = models.CharField(max_length=20, default='')
    wind_velocity = models.FloatField()
    weather_code = models.CharField(max_length=30, default='')


class EventStates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_id = models.CharField(max_length=250, default='')
    current_state = models.CharField(max_length=250, default='')
    period_value = models.CharField(max_length=200 ,default='')
    period_time_elapsed = models.CharField(max_length=100 ,default='')
    period_time_remaining = models.CharField(max_length=100, default='')
    minutes_elapsed = models.CharField(max_length=10, default='')
    period_minutes_elapsed = models.CharField(max_length=10, default='')
    context = models.CharField(max_length=200, default='')



class Persons(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_key = models.CharField(max_length=200 ,default='')
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='M')
    birth_date = models.DateField()
    death_date = models.DateField()
    final_resting_location = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    birth_location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='birth_loc')
    hometown_location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='hometown_loc')
    residence_location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='residence_loc')
    death_location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='death_loc')


class League(models.Model):
    league_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, default='')


class Seasons(models.Model):
    season_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()


class InjuryPhases(models.Model):
    INJ_STATUS_CHOICES = (
        ('A','Active'),
        ('P','Past')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Persons, on_delete=models.CASCADE)
    injury_status = models.CharField(max_length=10, choices=INJ_STATUS_CHOICES, default='P')
    injury_comment = models.CharField(max_length=250, default='')
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE)


class Position(models.Model):
    position_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    affiliation = models.ForeignKey(Affiliations, on_delete=models.CASCADE)
    abbreviation = models.CharField(max_length=100, default='')


class PersonPhases(models.Model):
    person_phases_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Persons, on_delete=models.CASCADE)
    uniform_number = models.IntegerField()
    regular_position = models.ForeignKey(Position, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    start_date_time = models.DateTimeField()
    start_season = models.ForeignKey(Seasons, on_delete=models.CASCADE, related_name='start_season')
    end_date_time = models.DateTimeField()
    end_season = models.ForeignKey(Seasons, on_delete=models.CASCADE, related_name='end_season')
    entry_reason = models.CharField(max_length=250, default='')
    exit_reason = models.CharField(max_length=250, default='')
    duration = models.IntegerField()


class PersonEventMetadata(models.Model):
    person_event_metadata_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Persons, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    health = models.CharField(max_length=100, default='')
    weight = models.FloatField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)


class TeamPhases(models.Model):
    team_phases_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_season = models.ForeignKey(Seasons, on_delete=models.CASCADE, related_name='start_season_team_phases')
    end_season = models.ForeignKey(Seasons, on_delete=models.CASCADE, related_name='end_season_team_phases')
    affiliation = models.ForeignKey(Affiliations, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()


class Rankings(models.Model):
    ranking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participant = models.ForeignKey(Teams, on_delete=models.CASCADE)
    issuer = models.CharField(max_length=250, default='')
    ranking_value = models.FloatField()
    ranking_value_previous = models.FloatField()


class CoreStats(models.Model):
    core_stats_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score = models.IntegerField()
    score_opposing = models.IntegerField()
    score_attempts = models.IntegerField()
    score_attempts_opposing = models.IntegerField()
    score_percentage = models.FloatField()
    score_percentage_opposing = models.FloatField()
    time_played_event = models.FloatField()
    time_played_total = models.FloatField()
    time_played_event_average = models.FloatField()
    events_played = models.IntegerField()
    events_started = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Awards(models.Model):
    award_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, default='')
    participant = models.ForeignKey(Teams, on_delete=models.CASCADE)
    total = models.FloatField()
    rank = models.IntegerField()
    award_value = models.FloatField()
    currency = models.CharField(max_length=20, default='')


class OutcomeTotals(models.Model):
    outcome_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rank = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    wins_overtime = models.IntegerField()
    losses_overtime = models.IntegerField()
    undecideds = models.IntegerField()
    winning_percentage = models.FloatField()
    points_scored_for = models.IntegerField()
    points_scored_against = models.IntegerField()
    points_difference = models.IntegerField()
    standing_points = models.IntegerField()
    events_played = models.IntegerField()
    games_back = models.IntegerField()
    sets_against = models.IntegerField()
    sets_for = models.IntegerField()


class EventActionPlays(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_state = models.ForeignKey(EventStates, on_delete=models.CASCADE)
    play_type = models.CharField(max_length=250, default='')
    play_result = models.CharField(max_length=15, default='')


class EventActionFouls(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_state = models.ForeignKey(EventStates, on_delete=models.CASCADE)
    foul_name = models.CharField(max_length=250, default='')
    foul_result = models.CharField(max_length=250, default='')
    fouler = models.ForeignKey(Persons, on_delete=models.CASCADE, related_name='fouler')
    recipient = models.ForeignKey(Persons, on_delete=models.CASCADE, related_name='recipient')


class EventActionPenalties(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_state = models.ForeignKey(EventStates, on_delete=models.CASCADE)
    penalty_level = models.CharField(max_length=100, default='')
    caution_level = models.CharField(max_length=100, default='')
    recipient = models.ForeignKey(Persons, on_delete=models.CASCADE)


class EventActionParticipants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_state = models.ForeignKey(EventStates, on_delete=models.CASCADE)
    event_action_play = models.ForeignKey(EventActionPlays, on_delete=models.CASCADE)
    person = models.ForeignKey(Persons, on_delete=models.CASCADE)


class SoccerOffensiveStats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goals_game_winning = models.IntegerField()
    goals_game_tying = models.IntegerField()
    goals_overtime = models.IntegerField()
    goals_shootout = models.IntegerField()
    goals_total = models.IntegerField()
    assists_game_winning = models.IntegerField()
    assists_game_tying = models.IntegerField()
    assists_overtime = models.IntegerField()
    assists_total = models.IntegerField()
    points = models.FloatField()
    shots_total = models.IntegerField()
    shots_on_goal_total = models.IntegerField()
    shots_hit_frame = models.IntegerField()
    shots_penalty_shot_taken = models.IntegerField()
    shots_penalty_shot_scored = models.IntegerField()
    shots_penalty_shot_missed = models.IntegerField()
    shots_penalty_shot_percentage = models.FloatField()
    shots_shootout_taken = models.IntegerField()
    shots_shootout_scored = models.IntegerField()
    shots_shootout_missed = models.IntegerField()
    shots_shootout_percentage = models.FloatField()
    giveaways = models.IntegerField()
    offsides = models.IntegerField()
    corner_kicks = models.IntegerField()
    hat_tricks = models.IntegerField()
    goals_own = models.IntegerField()
    free_kicks = models.IntegerField()


class SoccerDefensiveStats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shots_penalty_shot_allowed = models.IntegerField()
    goals_penalty_shot_allowed = models.IntegerField()
    goals_against_average = models.IntegerField()
    goals_against_total = models.IntegerField()
    saves = models.IntegerField()
    save_percentage = models.FloatField()
    catches_punches = models.IntegerField()
    shots_on_goal_total = models.IntegerField()
    shots_shootout_total = models.IntegerField()
    shots_shootout_allowed = models.IntegerField()
    shots_blocked = models.IntegerField()
    shutouts = models.IntegerField()
    goals_own = models.IntegerField()


class SoccerFoulStats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fouls_suffered = models.IntegerField()
    fouls_commited = models.IntegerField()
    cautions_total = models.IntegerField()
    cautions_pending = models.IntegerField()
    caution_points_total = models.IntegerField()
    caution_points_pending = models.IntegerField()
    ejections_total = models.IntegerField()


class SoccerEventStates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    period_time_elapsed = models.CharField(max_length=250, default='')
    period_time_remaining = models.CharField(max_length=250, default='')
    minutes_elapsed = models.IntegerField()
    period_minute_elapsed = models.IntegerField()
    score_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='score_team')
    score_team_opposing = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='score_team_opposing')
    score_team_home = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='score_team_home')
    score_team_away = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='score_team_away')


class SoccerActionPlays(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    soccer_event_state_id = models.ForeignKey(EventStates, on_delete=models.CASCADE)
    play_result = models.CharField(max_length=200, default='')
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    points = models.FloatField()


class SoccerActionParticipants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    soccer_action_play_id = models.ForeignKey(SoccerActionPlays, on_delete=models.CASCADE)
    person = models.ForeignKey(Persons, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)

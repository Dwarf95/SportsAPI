from django.contrib import admin

from sports.api.models import Locations, Sites, Addresses, Events, ParticipantsEvents, Periods, Affiliations, Teams, \
    AffiliationEvents, WeatherConditions, EventStates, Persons, League, Seasons, InjuryPhases, Position, PersonPhases, \
    PersonEventMetadata, TeamPhases, Rankings, CoreStats, Awards, OutcomeTotals, EventActionPlays, EventActionFouls, \
    EventActionPenalties, EventActionParticipants, SoccerOffensiveStats, SoccerDefensiveStats, SoccerFoulStats, \
    SoccerEventStates, SoccerActionPlays, SoccerActionParticipants

admin.site.register(Locations)
admin.site.register(Sites)
admin.site.register(Addresses)
admin.site.register(Events)
admin.site.register(ParticipantsEvents)
admin.site.register(Periods)
admin.site.register(Affiliations)
admin.site.register(Teams)
admin.site.register(AffiliationEvents)
admin.site.register(WeatherConditions)
admin.site.register(EventStates)
admin.site.register(Persons)
admin.site.register(League)
admin.site.register(Seasons)
admin.site.register(InjuryPhases)
admin.site.register(Position)
admin.site.register(PersonPhases)
admin.site.register(PersonEventMetadata)
admin.site.register(TeamPhases)
admin.site.register(Rankings)
admin.site.register(CoreStats)
admin.site.register(Awards)
admin.site.register(OutcomeTotals)
admin.site.register(EventActionPlays)
admin.site.register(EventActionFouls)
admin.site.register(EventActionPenalties)
admin.site.register(EventActionParticipants)
admin.site.register(SoccerOffensiveStats)
admin.site.register(SoccerDefensiveStats)
admin.site.register(SoccerFoulStats)
admin.site.register(SoccerEventStates)
admin.site.register(SoccerActionPlays)
admin.site.register(SoccerActionParticipants)


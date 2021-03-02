import graphene
from graphene_django import DjangoObjectType
from .models import Event

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ('title', 'description')

class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)

    def resolve_all_events(root, info):
        return Event.objects.all()

schema = graphene.Schema(query=Query)
    
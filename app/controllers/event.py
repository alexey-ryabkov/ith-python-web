import locale
from ..db.manager import DatabaseManager
from ..models.event import get_events_data, add_event_2fav, del_event_from_fav
from ..session import get_user

locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


def process_events(_, filter_fav=False):
    with DatabaseManager() as cursor:
        events = get_events_data(cursor, get_user(), filter_fav)
        for event in events:
            event["datetime"] = event["datetime"].strftime("%d %B %Y, %H:%M")
        return events


def process_add_event_2fav(_, event_id):
    with DatabaseManager() as cursor:
        return add_event_2fav(cursor, event_id, get_user())


def process_del_event_from_fav(_, event_id):
    with DatabaseManager() as cursor:
        return del_event_from_fav(cursor, event_id, get_user())

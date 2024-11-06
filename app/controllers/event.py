from ..db.manager import DatabaseManager
from ..models.event import get_events_data, add_event_2fav, del_event_from_fav
from ..session import get_user


def process_events(_, filter_fav = False):
    with DatabaseManager() as cursor:
        return get_events_data(cursor, get_user(), filter_fav)


def process_add_event_2fav(_, event_id):
    with DatabaseManager() as cursor:
        return add_event_2fav(cursor, event_id, get_user())


def process_del_event_from_fav(_, event_id):
    with DatabaseManager() as cursor:
        return del_event_from_fav(cursor, event_id, get_user())

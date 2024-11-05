from ..db.manager import DatabaseManager
from ..models.event import get_events_data
from ..session import get_user


def process_events(request):
    events_data = []
    with DatabaseManager() as cursor:
        events_data = get_events_data(
            cursor, get_user() if request.path == "/favorites" else None
        )
    return events_data

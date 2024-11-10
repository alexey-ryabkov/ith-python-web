from ..db.manager import DatabaseManager
from ..models.user import edit_user
from ..password import hash_password
from ..session import get_user
from ..validate import validate_user_data


def process_profile(request):
    data = request.form
    with DatabaseManager() as cursor:
        validate_user_data(cursor, data, True)
        edit_user(
            cursor,
            get_user(),
            data["login"],
            data["email"],
            hash_password(data["password"]),
        )

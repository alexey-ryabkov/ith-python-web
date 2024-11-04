import os
import hashlib

_SALT_LENGTH = 16
_SHA256_ITER_CNT = 100_000


def _get_salt_hash(value, salt):
    return hashlib.pbkdf2_hmac("sha256", value.encode(), salt, _SHA256_ITER_CNT)


def hash_password(password):
    salt = os.urandom(_SALT_LENGTH)
    hashed = _get_salt_hash(password, salt)
    return (salt + hashed).hex()


def verify_password(user_password, input_password):
    user_pswd_bytes = bytes.fromhex(user_password)
    salt = user_pswd_bytes[:_SALT_LENGTH]
    hashed = user_pswd_bytes[_SALT_LENGTH:]
    return _get_salt_hash(input_password, salt) == hashed

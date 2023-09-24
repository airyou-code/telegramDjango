import hashlib
import random
import string


def get_random_hash_name(id, length=12):
    hash_object = hashlib.sha256(str(id).encode())
    hash_value = hash_object.hexdigest()

    random.seed(hash_value)
    characters = string.ascii_uppercase + string.digits
    random_string = ''.join(random.choices(characters, k=length))

    return random_string

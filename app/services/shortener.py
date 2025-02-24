import random
import string


def generate_short_code(length: int = 6) -> str:
    """Generate a random string of letters and digits."""
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))

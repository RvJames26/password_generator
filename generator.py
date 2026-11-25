import secrets
import string

class PassGen:
    def __init__(self, requirements: dict):
        self.lower_count = requirements.get("character", 0)
        self.digit_count = requirements.get("numbers", 0)
        self.upper_count = requirements.get("upper", 0)
        self.special_count = requirements.get("special", 0)

    def generate(self) -> str:
        pools = {
            "lower": string.ascii_lowercase,
            "upper": string.ascii_uppercase,
            "digit": string.digits,
            "special": string.punctuation,
        }

        password_chars = []
        password_chars.extend(secrets.choice(pools["lower"]) for _ in range(self.lower_count))
        password_chars.extend(secrets.choice(pools["upper"]) for _ in range(self.upper_count))
        password_chars.extend(secrets.choice(pools["digit"]) for _ in range(self.digit_count))
        password_chars.extend(secrets.choice(pools["special"]) for _ in range(self.special_count))

        if not password_chars:
            all_chars = string.ascii_letters + string.digits + string.punctuation
            password_chars = [secrets.choice(all_chars) for _ in range(12)]

        secrets.SystemRandom().shuffle(password_chars)
        return "".join(password_chars)
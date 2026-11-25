import secrets
import string

class PassGen:
    def __init__(self, requirements: dict):
        self.total_length = requirements.get("character", 12)
        self.digit_count = requirements.get("numbers", 0)
        self.upper_count = requirements.get("upper", 0)
        self.special_count = requirements.get("special", 0)

        # Fill the rest with lowercase so total never exceeds `character`
        self.lower_count = max(
            0,
            self.total_length - (self.digit_count + self.upper_count + self.special_count),
        )

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

        secrets.SystemRandom().shuffle(password_chars)
        return "".join(password_chars)
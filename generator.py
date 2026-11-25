import secrets
import string

class PassGen:
    def __ini__(self, requirements: dict):
        self.lower_count = requirements.get("character", 0)
        self.digit_count = requirements.get("numbers", 0)
        self.upper_count = requirements.get("upper", 0)
        self.special_count = requirements.get("special", 0)
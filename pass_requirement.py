class PassReq:
    def __init__(self):
        self.character = int(input("Total password length: "))
        self.numbers = int(input("Number of digits: "))
        self.upper = int(input("Number of uppercase letters: "))
        self.special = int(input("Number of special characters: "))
        self._validate()

    def _validate(self):
        required = self.numbers + self.upper + self.special
        if required > self.character:
            raise ValueError(
                f"Digits + uppercase + special ({required}) cannot exceed "
                f"total length ({self.character})"
            )

    def return_req(self):
        return {
            "character": self.character,
            "numbers": self.numbers,
            "upper": self.upper,
            "special": self.special,
        }
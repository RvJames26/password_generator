class PassReq:

    def __init__(self):
        self.character = int(input("Character requirements: "))
        self.numbers = int(input("Number requirements: "))
        self.upper = int(input("Uppercase requirements: "))
        self.special = int(input("Special character requirements: "))

    def return_req(self):
        return {
            "character": self.character,
            "numbers": self.numbers,
            "upper": self.upper,
            "special": self.special,
        }
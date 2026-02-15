class Seat:
    def __init__(self, number: int):
        if number <= 0:
            raise ValueError()

        self.number = number
        self.is_taken = False
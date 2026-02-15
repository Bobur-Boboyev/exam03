from seat import Seat


class Ticket:
    def __init__(self, seat: Seat, owner: str):
        if not isinstance(seat, Seat):
            raise TypeError()

        if not owner:
            raise ValueError()

        self.seat = seat
        self.owner = owner
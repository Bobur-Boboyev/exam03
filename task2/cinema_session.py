from seat import Seat
from ticket import Ticket


class CinemaSession:
    def __init__(self, movie_title: str, total_seats: int):
        if not movie_title or not movie_title.strip():
            raise ValueError()

        if total_seats <= 0:
            raise ValueError()

        self.movie_title = movie_title
        self.total_seats = total_seats
        self.seats = [Seat(i) for i in range(1, total_seats + 1)]
        self.bookings = []


    def available_seats(self) -> list[int]:
        return [seat.number for seat in self.seats if not seat.is_taken]
    

    def book_seat(self, seat_number: int, user: str) -> Ticket:

        if seat_number < 1 or seat_number > self.total_seats:
            raise ValueError()
        
        seat = self.seats[seat_number - 1]

        if seat.is_taken:
            raise RuntimeError()

        seat.is_taken = True

        ticket = Ticket(seat, user)

        self.bookings.append(ticket)

        return ticket

    def __str__(self):
        return f"CinemaSession: {self.movie_title} ({self.total_seats} seats)"

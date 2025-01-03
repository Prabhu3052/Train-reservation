class Train:
    def __init__(self, train_number, name, available_seats):
        self.train_number = train_number
        self.name = name
        self.available_seats = available_seats

    def book_seat(self, number_of_seats):
        if self.available_seats >= number_of_seats:
            self.available_seats -= number_of_seats
            return True
        else:
            return False

    def cancel_seat(self, number_of_seats):
        self.available_seats += number_of_seats

    def __str__(self):
        return f"Train {self.train_number} - {self.name} - Available Seats: {self.available_seats}"


class Passenger:
    def __init__(self, name, age, train_number, seat_number):
        self.name = name
        self.age = age
        self.train_number = train_number
        self.seat_number = seat_number

    def __str__(self):
        return f"Passenger: {self.name}, Age: {self.age}, Train: {self.train_number}, Seat: {self.seat_number}"


class Reservation:
    def __init__(self):
        self.trains = {}
        self.passengers = {}

    def add_train(self, train):
        self.trains[train.train_number] = train

    def book_ticket(self, name, age, train_number, number_of_seats):
        train = self.trains.get(train_number)
        if train and train.book_seat(number_of_seats):
            for seat_number in range(1, number_of_seats + 1):
                passenger = Passenger(name, age, train_number, seat_number)
                self.passengers[seat_number] = passenger
            print(f"Booking successful for {name}. Train: {train.name}, Seat numbers: {list(range(1, number_of_seats + 1))}")
        else:
            print("Booking failed. Not enough seats available.")

    def cancel_ticket(self, seat_number):
        passenger = self.passengers.pop(seat_number, None)
        if passenger:
            train = self.trains[passenger.train_number]
            train.cancel_seat(1)
            print(f"Ticket canceled for {passenger.name}. Train: {train.name}, Seat: {seat_number}")
        else:
            print("No reservation found for this seat.")

    def show_reservations(self):
        for passenger in self.passengers.values():
            print(passenger)


# Sample usage
if __name__ == "__main__":
    reservation_system = Reservation()

    # Adding trains
    reservation_system.add_train(Train("123", "Express Train", 10))
    reservation_system.add_train(Train("456", "Local Train", 20))

    # Booking tickets
    reservation_system.book_ticket("John Doe", 30, "123", 2)
    reservation_system.book_ticket("Jane Smith", 28, "456", 3)

    # Viewing reservations
    reservation_system.show_reservations()

    # Canceling a ticket
    reservation_system.cancel_ticket(1)

    # Viewing updated reservations
    reservation_system.show_reservations()

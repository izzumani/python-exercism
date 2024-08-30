"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    index = 0
    counter =0
    
    while(len(range(0,number))>counter):
        if index ==0:
            yield 'A'
            index +=1
        elif index ==1:
            yield 'B'
            index +=1
        elif index ==2:
            yield 'C'
            index +=1
        else:
         
            yield 'D'
            index =0
        counter +=1
    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_number = 1
    row_number =1
    indexer = generate_seat_letters(number)
    while(number >= seat_number):
        seat_letter = next(indexer)
        yield f"{row_number}{seat_letter}"
        if seat_letter =="D":
            row_number +=1
            if row_number==13:
                row_number +=1

        seat_number +=1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_assignment = {}
    indexer = generate_seats(len(passengers))
    for _passenger in passengers:
        seat_assignment[_passenger] = next(indexer)
    return seat_assignment

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        concord_code = seat_number + flight_id
        yield concord_code.ljust(12,'0')

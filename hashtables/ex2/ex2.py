#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    trip_table = {}
    for ticket in tickets:
        trip_table[ticket.source] = ticket.destination
    
    route = []
    location = trip_table["NONE"]
    while location != "NONE":
        route.append(location)
        location = trip_table[location]
    route.append("NONE")
    
    return route

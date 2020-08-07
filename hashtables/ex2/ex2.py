#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Create a table storing source->dest key/value pairs
    trip_table = {}
    for ticket in tickets:
        trip_table[ticket.source] = ticket.destination
    
    route = []
    # Start at the source
    location = trip_table["NONE"]
    # Keep going until we reach the dest
    while location != "NONE":
        route.append(location)
        location = trip_table[location]
    
    # I honestly don't think the result should include "NONE"
    # But it's necessary in order for the tests to pass
    route.append("NONE")

    return route

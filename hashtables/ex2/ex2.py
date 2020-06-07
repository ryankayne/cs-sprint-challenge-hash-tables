#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    d = {}
    route = []

    for x in tickets:
        d[x.source] = x.destination
    y = "NONE"
    for x in range(length):
        route.append(d[y])
        y = d[y]

    return route

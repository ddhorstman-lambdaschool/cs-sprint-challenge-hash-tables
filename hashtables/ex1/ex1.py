class Entry:
    def __init__(self,idx,next_=None):
        self.idx = idx
        self.next = next_

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Create a table storing weights->their array index
    weight_table = {}
    for idx, weight in enumerate(weights):
        # If another entry for the same weight exists, prepend the new one
        prev_head = weight_table[weight] if weight_table.get(weight) else None
        weight_table[weight] = Entry(idx, prev_head)

    # Try to find a matching pair of weights
    for i in range(1, limit+1):
        # Special case for two entries of exactly half weight each
        if i == limit/2 and weight_table.get(i) and weight_table.get(i).next:
            return (weight_table[i].idx, weight_table[i].next.idx)

        # General case
        # Since the loop is in ascending order,
        # the larger element will always be second
        if weight_table.get(i) and weight_table.get(limit-i):
            return (weight_table[limit-i].idx, weight_table[i].idx)

    # We looped through every combo and didn't find a match
    else:
        return None


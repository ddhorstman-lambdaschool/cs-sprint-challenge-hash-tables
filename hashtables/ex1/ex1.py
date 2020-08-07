class Entry:
    def __init__(self,idx,next=None):
        self.idx = idx
        self.next = next

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Populate hash table
    weight_table = {}
    for idx, weight in enumerate(weights):
        # If another entry for the same weight exists, prepend the new one
        prev_head = weight_table[weight] if weight_table.get(weight) else None
        weight_table[weight] = Entry(idx, prev_head)

    # Consider all possible weight combinations
    for i in range(1, limit+1):
        # Special case for two entries of exactly half weight each
        if i == limit/2 and weight_table.get(i) and weight_table.get(i).next:
            return (weight_table[i].idx, weight_table[i].next.idx)

        # General case
        if weight_table.get(i) and weight_table.get(limit-i):
            return (weight_table[limit-i].idx, weight_table[i].idx)

    # We looped through every combo and didn't find a match
    else:
        return None


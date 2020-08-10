def has_negatives(a):
    """
    YOUR CODE HERE
    """

    num_dict = {}
    result = []
    for number in a:
        # If we've seen its opposite, add it to the result
        if -number in num_dict:
            result.append(abs(number))
        # Otherwise, store it and see if we find its partner
        else:
            num_dict[number] = "Value doesn't matter. Should have used a set."

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

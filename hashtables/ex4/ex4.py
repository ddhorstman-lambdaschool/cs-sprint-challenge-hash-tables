def has_negatives(a):
    """
    YOUR CODE HERE
    """

    num_dict = {}
    result = []
    for number in a:
        if -number in num_dict:
            result.append(abs(number))
        else:
            num_dict[number] = "Value doesn't matter. Should have used a set."
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

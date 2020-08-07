def intersection(arrays):
    """
    YOUR CODE HERE
    """
    all_dict = {}
    result_dict = {}
    result = []
    for array in arrays:
        for number in array:
            # If we've seen this number already,
            # add it to the list of shared elements
            if number in all_dict:
                if number not in result_dict:
                    result_dict[number] = 1
                result_dict[number] += 1
            # Otherwise, add it to the list of numbers
            else:
                all_dict[number] = "Value doesn't matter. Should have used a set."
    # Look through shared elements
    for number in result_dict:
        # If it appeared in every list, add it to the result
        if result_dict[number] == len(arrays):
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

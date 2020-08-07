def intersection(arrays):
    """
    YOUR CODE HERE
    """
    all_numbers = {}
    shared_numbers = {}
    result = []

    # Read thru the arrays and find shared elements
    for idx, array in enumerate(arrays):
        for number in array:

            # Add the number to the dict only if this is the first array
            # This saves a lot of memory and runs 10% faster
            # than adding elements from every array to the dict
            if idx == 0:
                all_numbers[number] = "Value doesn't matter. Should have used a set."

            # If we've seen this number already,
            # update its entry in the shared numbers dict
            elif number in all_numbers:
                if number not in shared_numbers:
                    shared_numbers[number] = 1
                shared_numbers[number] += 1

    # Look through shared elements
    for number in shared_numbers:
        # If it appeared in every list, add it to the result
        if shared_numbers[number] == len(arrays):
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    all_dict = {}
    result_dict = {}
    result = []
    for array in arrays:
        for number in array:
            if number in all_dict:
                if number not in result_dict:
                    result_dict[number] = 1
                result_dict[number] += 1
            else:
                all_dict[number] = "value doesn't matter"

    for number in result_dict:
        if result_dict[number] == len(arrays):
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # test = [
    #     [1, 2, 3, 4, 5],
    #     [12, 7, 2, 9, 1],
    #     [99, 2, 7, 1,]
    # ]

    # d = {}
    # result = []
    # intersections = []

    # for x in range(len(test)):
    #     for y in range(len(test[x])):
    #         if test[x][y] not in d:
    #             d[test[x][y]] = 1
    #         else:
    #             d[test[x][y]] += 1
    #         if d[test[x][y]] == len(test):
    #             result.append(test[x][y])
    # return result

    d = {}
    result = []
    # intersections = []

    for x in range(len(arrays)):
        for y in range(len(arrays[x])):
            if arrays[x][y] not in d:
                d[arrays[x][y]] = 1
            else:
                d[arrays[x][y]] += 1
            if d[arrays[x][y]] == len(arrays):
                result.append(arrays[x][y])
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

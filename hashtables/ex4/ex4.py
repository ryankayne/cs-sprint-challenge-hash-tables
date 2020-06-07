arr = [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    d = {}
    result = []

    for x in a:
    #     d[x] = abs(x)
    # for x in d:
    #     if x < 0:
    #         result.append(d[x])
        if x < 0:
            result.append(abs(x))
    return result

has_negatives(arr)

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

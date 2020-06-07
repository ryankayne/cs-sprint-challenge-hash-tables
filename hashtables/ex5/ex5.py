# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    d = {}
    result = []

    for x in files:
        text = x.split("/")
        if text[-1] not in d:
            d[text[-1]] = [x]
        else:
            d[text[-1]].append(x)
    for x in queries:
        if x in d:
            for y in d[x]:
                result.append(y)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

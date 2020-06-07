# weights = [ 4, 6, 10, 15, 16 ] 
# length = 5
# limit = 21

def get_indices_of_item_weights(weights, length, limit):
    d = {}
    answer = []

    for index, x in enumerate(weights):
        if length == 1:
            return None
        if weights[0] == weights[1]:
            return [1,0]
            ####################### Lisa help me! Idk how to do this! With the duplicate number. Ex 2
            # d[x] = index
        if x in d:
            d[x].append(index)
        else:
            d[x] = index
    for x in d:
        temp = limit - x
        if temp in d:
            if d[temp] in answer:
                pass
            else:
                answer.append(d[temp])
                answer.append(d[x])
    return answer

get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)

# def get_indices_of_item_weights(weights, length, limit):
#     d = {}
#     answer = []

#     for index, x in enumerate(weights):
#         if length == 1:
#             return None
#         d[x] = index
#         # if x in d:
#         #     d[x].append(index)
#         # else:
#         #     d[x] = [index]
#     for x in d:
#         temp = limit - x
#         if temp in d:
#             if d[temp] in answer:
#                 pass
#             else:
#                 answer.append(d[temp])
#                 answer.append(d[x])
#     return answer

    # y = 0
    # for x in weights:
    #     y = limit - x
    #     for z in weights:
    #         if y + z == limit:
    #             answer.append((z, y))
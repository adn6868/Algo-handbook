'''
calculate the distance between a string to another string
'''
print("hi")
# def recursiveDistance(first,second):
#     if len(first) < len(second):
#         first, second = second, first
#     if len(second) == 0:
#         return len(first)

#     return recursiveDistance(first[1:],second[1:]) + min(insertions,deletion,subtitute)


def distance(first, second):
    if len(first) < len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    pre_row = range(len(second) + 1)
    for i, c1 in enumerate(first):
        cur_row = [i + 1]
        for j, c2 in enumerate(second):
            insertions = pre_row[j+1] + 1
            deletions = cur_row[j] + 1
            subtitute = pre_row[j] + (c1 != c2)
            cur_row.append(min(insertions, deletions, subtitute))
        pre_row = cur_row
    return pre_row[-1]


print(distance('a', 'a'))
print(distance('a', ''))
print(distance('', 'b'))
print(distance('abc', 'cdb'))
print(distance('cde', 'abcdefgh'))
# print(distance('a','b'))

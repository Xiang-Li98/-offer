def get_duplications(list, length):
    assert length != 0, "The list is empty"
    start = 1
    end = length - 1
    while end >= start:
        middle = ((end-start) >> 1) + start
        count = count_range(list, length, start, middle)
        if start == end:
            if count > 1:
                return start
            else:
                return False
        if count > middle - start + 1:
            end = middle
        else:
            start = middle + 1
    return False


def count_range(list, length, start, end):
    count = 0
    for i in range(0, length):
        if start <= list[i] <= end:
            count += 1
    return count


li = [2, 3, 5, 4, 3, 2, 6, 7]
print("重复的数字：", get_duplications(li, len(li)))

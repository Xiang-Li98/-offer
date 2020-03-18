def get_duplication(list, length):
    assert length != 0, "The list is empty"
    tempt = [None for i in range(length)]
    for j in range(0, length):
        assert 1 <= list[j] < length, "The number %d in list is illegal" % list[j]
        if tempt[list[j]] is None:
            tempt[list[j]] = list[j]
        else:
            return list[j]
    return False




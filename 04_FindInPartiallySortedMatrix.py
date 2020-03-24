# 面试题4：二维数组中的查找
# 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
# 照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
# 整数，判断数组中是否含有该整数。


def find_sorted_matrix(matrix, rows, columns, number):
    row = 0
    col = columns - 1
    found = False
    while row < rows and col >= 0:
        if number == matrix[row][col]:
            found = True
            break
        if number > matrix[row][col]:
            row += 1
        else:
            col -= 1
    return found




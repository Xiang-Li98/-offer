'''
我们可以原地调整数组的顺序，使得数字 i 刚好在下标为 i 的位置（其实就是原地建立哈希表）。如果有重复数字，意味着有些位置存在多个数字。我们的目标是找到存在多个数字的位置。步骤如下：

从头开始遍历数组中的每个数字，当扫描到第i个数字m时，比较m是否等于i。

若是，则接着扫描下一个数字（m恰好在属于它的位置）；
若不是，则将第i个数字与第m个数字作比较

若相等，就找到了一个重复的数字；
若不相等，则将第i个数字和第m个数字交换位置（把m放到属于它的位置上）。





重复这个比较、交换的过程，直到我们发现一个重复的数字。
这时空间复杂度只需O(1)，时间复杂度依然为O(n)。
'''


def duplicate(numbers, length, duplication):
    if length <= 0:
        return False
    for i in range(0, length):
        if numbers[i] < 0 or numbers[i] > length - 1:
            return False
        while numbers[i] != i:
            if numbers[numbers[i]] != numbers[i]:
                tempt = numbers[numbers[i]]
                numbers[numbers[i]] = numbers[i]
                numbers[i] = tempt
                print(numbers)
            else:
                duplication = numbers[i]
                return duplication
    return False


test1 = [2, 3, 1, 0, 2, 5, 3]
leng = len(test1)
flag = duplicate(test1, leng, -1)
if flag != 0:
    print("重复的数字：", flag)
else:
    print("False")

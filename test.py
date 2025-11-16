'9/30 lecture'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


me = Person('mdrz', 20)
# print(me.name)


nums = [-2, 4, -6, 12, 12, -7, 5, 18]
nums_find = [] + nums
flag = False
target = -13  # 6+7, print array of indices [2,4],
# always one correct answer, can be duplicate i.e. [3,3], sol == [0,1]
# can be negative numbers

# 1. check duplicate
# if target is even & target/2 exists in array twice, print their indices, done

# 2. if positive target
# min + max
#   if > target
#   remove max, repeat
#   if < target
#   remove min, repeat
#   if = target
#   print solution

# 3. if negative target
# actually probably the same, dont see no reason for why it shouldnt work


if target % 2 == 0 and target / 2 in nums:
    flag = True
    print("yes")
    res = []
    nums_dict = dict(enumerate(nums))
    for i in nums_dict:
        if nums_dict[i] == target / 2:
            res.append(i)
    print(res)


def attempt():
    return (min(nums_find) + max(nums_find))


if flag == False:
    while attempt() != target and flag == False:
        if attempt() < target:
            nums_find = nums_find[1:]
        if attempt() > target:
            nums_find.pop()
    print(nums.index(min(nums_find)), nums.index(max(nums_find)))
if flag == False:
    print(nums, nums_find)
    print([nums.index(min(nums_find)), nums.index(max(nums_find))])

print["a", "a"]
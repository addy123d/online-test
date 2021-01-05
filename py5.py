# def runningSum(nums):
#     sum = 0
#     for i in range(0, len(nums)):
#         sum = sum + nums[i]
#         totalArr.append(sum)
#     return totalArr


# nums = [1, 2, 3, 4]
# totalArr = []

# result = runningSum(nums)
# print(result)

# Sum pairs !
# i/p - [3,5,6,2,9,4]  and 8
# o/p - 3,5,6,2


# nums = [3, 5, 6, 2, 9, 4]

# result = []

# total = 8

# nums[2] + nums[3] == 8

# for index in range(1, len(nums)):
#     sum = nums[index-1] + nums[index]

#     if sum == total:
#         ele = [nums[index-1], nums[index]]
#         result.append(ele)

# print(result)


# nums = [
#     [1, 0],
#     [2, -1],
#     [-3, 2],
#     [4, -1]
# ]


# for i in range(0, len(nums)):  # i = 0
#     print(nums[i])  # nums[i] = nums[0] = [1,0]
#     for j in range(0, len(nums[i])):  # j = 0,1
#         print(nums[i][j])  # nums[i][j] = nums[0][0] = 1, nums[0][1] =

# Missing integer from 1 to 10 !

nums = [1, 2, 3, 4, 5, 7, 8, 9, 10]

for index in range(0, len(nums)):
    if nums[index] != index+1:
        print(nums[index]-1)
        break

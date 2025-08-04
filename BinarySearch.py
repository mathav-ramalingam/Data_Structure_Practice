def linear_search(nums,key):
    for index , value in enumerate(nums):
        if value == key:
            return index
    return -1


def binary_search(nums,key):
    left_index = 0
    right_index = len(nums)
    mid_val = 0


    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if mid_index >= len(nums) or mid_index < 0:
            return -1
        else:
            mid_val = nums[mid_index]


        if mid_val == key:
            return mid_index

        if mid_val < key:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_recursion(nums,key,left_index,right_index):
    if left_index > right_index:
        return -1

    mid_index = (left_index + right_index) // 2

    if mid_index >= len(nums) or mid_index < 0:
        return -1
    else:
        mid_val = nums[mid_index]

    if mid_val == key:
        return mid_index

    if mid_val < key:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_recursion(nums,key,left_index,right_index)



if __name__ == "__main__":
    nums = [1,7,8,25,37,49,50,52,61,67,72,79,80,81,84,87,90,94,98,99]
    key = 50


    lin_index = linear_search(nums,key)
    print(f"Index of the value is {lin_index} using linear search")

    bin_index = binary_search(nums,key)
    print(f"Index of the value is {bin_index} using Binary search")

    rec_bin_index = binary_recursion(nums,key,0,len(nums)-1)
    print(f"Index of the value is {rec_bin_index} using Binary recursion Search")
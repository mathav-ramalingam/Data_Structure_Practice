def bubble_sort(nums):
    size = len(nums)
    for i in range(size-1):
        for j in range(size-1-i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    print(nums)



if __name__ == "__main__":
    nums = [4,8,1,52,9,85,7,69,3,5,70,10,89]

    bubble_sort(nums)
def insertion_sort(nums):
    
    for i in range(1,len(nums)):
        anchor = nums[i]
        j = i-1
        while j >= 0 and anchor > nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
        
        nums[j+1] = anchor


if __name__ == "__main__":
    
    test_cases = [
        [11,8,297,2,15,28],
        [3,7,9,11],
        [22,25,21,10],
        [29,15,28],
        [],
        [0],
        [25,8,2,6,25,2],
        [20,5,20,13,5,7,5]
    ]


    for element in test_cases:
        insertion_sort(element)
        print(f"Sorted array: {element}")
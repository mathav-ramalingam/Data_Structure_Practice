def swap(nums,a,b):
    if a != b:
        nums[a], nums[b] = nums[b], nums[a]

def partition(nums,start,end):

    pivot_index = start
    pivot = nums[pivot_index]

    while start < end:
        while start < len(nums) and nums[start] <= pivot:
            start += 1

        while nums[end] > pivot:
            end -= 1

        if start < end:
            swap(nums, start, end)

    swap(nums, pivot_index, end)

    return end

def quick_sort(nums,start,end):
    if start < end:
        mid = partition(nums,start,end)
        quick_sort(nums,start,mid-1)     # left partition
        quick_sort(nums,mid+1,end)       # right partition


if __name__ == "__main__":

    # nums = [4, 8, 1, 52, 9, 85, 7, 69, 3, 5, 70, 10, 89]

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

    # quick_sort(nums,0,len(nums)-1)
    # print(nums)

    for element in test_cases:
        quick_sort(element, 0, len(element)-1)
        print(f"Sorted array: {element}")
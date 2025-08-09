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
    nums = [4, 8, 1, 52, 9, 85, 7, 69, 3, 5, 70, 10, 89]

    quick_sort(nums,0,len(nums)-1)
    print(nums)
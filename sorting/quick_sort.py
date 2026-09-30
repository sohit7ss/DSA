nums = [6, 5, 9, 3, 4, 2, 1]
    #   l                 h


    
def quick_sort(nums, low, high):
    if low < high:
        p_ind = partition(nums, low, high)
        quick_sort(nums, low, p_ind-1)
        quick_sort(nums, p_ind+1 , high)

def partition (nums, low, high):
    pivot = nums[low]
    i ,j = low, high

    while i<j:
        while nums[i] <= pivot and i <= high -1:
            i +=1
        while nums[j] > pivot and j >= low + 1:
            j -= 1
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j
    

quick_sort(nums,0, len(nums)-1)
print(nums)

# time complexity in best or average case is TC = O(nlogn)
# but in worst case 
# for eg:- nums = [3, 3, 3, 3, 3, 3, 3, 3]
# here TC = O(n * n) = O(n^2)
# SC = O(1)
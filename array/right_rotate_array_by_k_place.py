nums = [3, 4, 5, 2, 8, 10, 6, 1]
def right_rotate_by_k_with_slicing (nums, k):
        n = len(nums)
        if k > n:
            r= k % n
            while r:
                nums[:] = nums[-1:] + nums[0:n-1]
                r = r-1
            return nums

        nums[:] = nums[n-k:] + nums[:n-k]
        return nums
print(right_rotate_by_k_with_slicing(nums, 5))
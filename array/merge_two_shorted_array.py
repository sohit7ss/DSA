nums1 = [1, 3 ,4, 5, 6, 7]
nums2 = [1, 2, 4, 8]


# def merge_two_sorted_array(nums1, nums2):
#     new_array = []
#     for i in nums1:
#         for j in nums2:
#             if i != j:
#                 if i>j:
#                     new_array.append[j]
#                     new_array.append[i]
#             elif i == j:
#                 new_array.append[i]
#     return new_array

# print(merge_two_sorted_array(nums1, nums2))

def merge_two_sorted_array(nums1, nums2):
    i = 0
    j = 0
    merged = []
    while i<len(nums1) and j<len(nums2):
        if nums1[i]> nums2[j]:
            merged.append(nums1[i])
            i += 1
        elif nums1[i] < nums2[j]:
            merged.append(nums2[j])
            j += 1
        else:
            merged.append(nums1[i])
            i += 1
            j += 1
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1
    
    return merged

print(merge_two_sorted_array(nums1, nums2))
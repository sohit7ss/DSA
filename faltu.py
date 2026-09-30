# # nums = [10, 7, 9, 3, 4, 1, 2]

# # def bubble_sort(nums):
# #     n= len(nums)
    
# #     for i in range (n-1, 0-1, -1):
# #         is_swap = False
# #         max_ind_num = i
# #         for j in range (0,i):
# #             if nums[j] > nums[j+1]:
# #                 nums[j], nums[j+1] = nums[j+1], nums[j]
# #             is_swap = True

# #         if is_swap == False:
# #             break

# #     return nums
            
# # print(bubble_sort(nums))


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.neighbors = []

# A = Node('A')
# B = Node('B')
# C = Node('C')
# D = Node('D')
# E = Node('E')

# A.neighbors = [B, E]
# B.neighbors = [A, C, D]
# C.neighbors = [B, D]
# D.neighbors = [B, C, E]
# E.neighbors = [A, D]

# def dfs(node, visited=set()):
#     if node in visited:
#         return
    
#     print(node.value)
#     visited.add(node)

#     for neighbor in node.neighbors:
#         dfs(neighbor, visited)

# # dfs(B)
# pos = [2, 4, 6]
# neg = [-2, -4, -6]
# for i in pos and j in neg:
#     print(i)
#     print(j)



print("Hello, World!")
print("I am learning Python!")

def are_positive(nums):
   a = [i for i in nums if i%2 == 0]
   return a

def are_greater_than_n(nums, n):
   a = []
   for i in nums:
      if i>n:
         a.append(i)
   return a

def are_divisible_by_n(nums, n):
   a = []
   i = 0
   while i<len(nums):
      if nums[i]%n ==0:
         a.append(nums[i])
      i+=1
   return a
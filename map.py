def square_all(nums):
   a = [i**2 for i in nums]
   return a

def add_n_all(nums, n):
   i = 0
   a = []
   while i < len(nums):
      a.append(nums[i]+n)
      i+=1
   return a

def even_or_odd_all(nums):
   a = []
   for i in nums:
      if i%2 == 0:
         a.append(True)
      else:
         a.append(False)
   return a
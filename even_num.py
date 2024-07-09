# add of all even from 0 to input num
target = int(input("Enter a number between 0 and 1000:- ")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
even_sum = 0
for num in range(2, target + 1, 2):
  even_sum += num 
print(even_sum)
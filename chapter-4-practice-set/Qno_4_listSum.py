# Write a program to get the sum of numbers in a  list containing n numbers.
list = [1, 3, 5, 6, 34, 33]
# print(len(list))
print(sum(list))
print(list[0] + list[1] + list[2] + list[3] + list[4] + list[5])
sum = 0
for i in range (len(list)):
    sum+= list[i]
print(sum)

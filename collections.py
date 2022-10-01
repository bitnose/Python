numbers = [3, 1, 4, 5]
numbers[-2] = 1
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(*numbers, end= ", ")
print(5 in numbers)

numbers1 = [3, 1, 4, 5, 4, 5]
print(sum(numbers1))
print(set(numbers1))
print(list(set(numbers1)))

a = [2, 0, 2, 2]
b = [1]
print(a + b)

c = [4, 2, 120]
d = [4, 100, 4]
print(c > d)

n = ["4", "2"]
m = ["4", "100"]
print(n > m)



zeros = [0] * 500
print(zeros)
print(len(zeros))

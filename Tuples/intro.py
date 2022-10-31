big_country = ["India", 1626037127260] 
small_country = ["Tuvalu", 12119]

small_country = big_country 
small_country[1] = 12222

print(f"The population of the small country is {small_country[1]}") 
print(f"The population of {big_country[0]} is {big_country[1]}")

a=1 
b=2


a, b = b, a
print(f"{a} {b}")

student_list = ["John", "Harriet"]
student_tuple = ("Cathy", "Ann")
student_list.append("Peter") 
#student_tuple.append("Peter") 
print(student_list) 
print(student_tuple)


student_tuple = ("John", ["Finnish", "Swedish"])
print(student_tuple)
student_tuple[1].append("English")
print(student_tuple)

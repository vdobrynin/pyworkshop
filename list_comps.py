# names = ["Nina", "Max", "Rose", "Jimmy"]
# my_list = [] # empty list
# for name in names:
#     my_list.append(len(name))
# print(my_list)
# [4, 3, 4, 5]

names = ["Nina", "Max", "Rose", "Jimmy"]
my_list = [len(name) for name in names]
print("Before:", my_list)

# my_list = [len(name) for name in names if len(name) % 2 == 0]
my_list = [len(name) for name in names if len(name) % 2 != 0]
print("After:", my_list)



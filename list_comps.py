# names = ["Nina", "Max", "Rose", "Jimmy"]
# my_list = [] # empty list
# for name in names:
#     my_list.append(len(name))
# print(my_list)
# [4, 3, 4, 5]

names = ["Nina", "Max", "Rose", "Jimmy"]
my_list = [len(name) for name in names]
print("Before:", my_list)

print("-------")
# my_list = [len(name) for name in names if len(name) % 2 == 0]
my_list = [len(name) for name in names if len(name) % 2 != 0]
print("After:", my_list)

print("-------")
scores = {f"player-{num}":0 for num in range(0, 5)}
print(scores)

print("-------")
my_list = [(f"player-{num}", num * 2) for num in range(0, 5)]
print(my_list)

print("-------")
scores = {key:value for (key, value) in my_list}
print(scores)

print("-------")
my_set = {num for num in [1, 2, 1, 0, 3]}
print(my_set)
# {0, 1, 2, 3}

print("-------")
list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
print(list_comp)
# [0, 4, 16, 36, 64]

print("-------")
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
print(gen_exp)
for num in gen_exp:
    print(num)

print("-------")
# gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
# for num in gen_exp:
#     print(num)
# for num in gen_exp:
#     print(num)   
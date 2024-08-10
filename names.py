# Python file names.py
names = ["Jimmy", "Rose", "Max", "Nina", "Phillip"]

for name in names:
    if len(name) != 4:
        continue

    print(f"Hello, {name}")

    if name == "Nina":
        break

print("Done!")

my_sum = sum([0, 1, 2, 3, 4])
print(my_sum)



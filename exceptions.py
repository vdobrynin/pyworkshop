# exceptions.py

# # this will throw an exception!
# int("a")

# print("End of the program.")

# try:
#     int("a")
# except ValueError:
#     print("Oops, couldn't convert that value into an int!")

# print("Reached end of the program.")

try:
    int("a")
except ValueError as error:
    print(f"Something went wrong. Message: {error}")

print("Reached end of the program.")


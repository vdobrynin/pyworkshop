names = ["Bob", "Alice", "Eve"]
scores = [42, 97, 68]

for name, score in zip(names, scores):
    print(f"{name} had a score of {score}.")
# Bob had a score of 42.
# Eve had a score of 68.

print("------")
print(scores.pop(-1))
print("------")
for name, score in zip(names, scores):
    print(f"{name} had a score of {score}.")

print("------")
names = ["Bob", "Alice", "Eve"]
scores = [42, 97, 68]
score_dict = dict(zip(names, scores))
print(score_dict)

print("------")
names = ["Bob", "Alice", "Eve"]
scores = [42, 97, 68]
zip_result = zip(names, scores)
for name, score in zip_result:
    print(f"{name} had a score of {score}.")
# Bob had a score of 42.
# Eve had a score of 68.
print("------")
for name, score in zip_result:
    print(f"{name} had a score of {score}.")
    print("------")
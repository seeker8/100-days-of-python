import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
index = random.randint(0, len(friends) - 1)


print(friends[index])

# using random.choice
print(f"with random.choice - {random.choice(friends)}")
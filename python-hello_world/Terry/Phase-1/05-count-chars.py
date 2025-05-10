text = "manual count"

# Regular counter
count = 0
for char in text:
    count += 1
print(count)

# Pythonic counter
for qty, char in enumerate(text, 1):
    pass
print(qty)
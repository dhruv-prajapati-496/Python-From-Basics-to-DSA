import random

# Random is a module which have different methods : 

# 1. random.random() -> Returns a random float between 0.0 (inclusive) and 1.0 (exclusive)
print("random():", random.random())

# 2. random.uniform(a, b) -> Returns a random float between a and b (inclusive bounds in float range)
print("uniform(1, 10):", random.uniform(1, 10))

# 3. random.randint(a, b) -> Returns a random integer between a and b (BOTH a and b are inclusive!)
print("randint(1, 6):", random.randint(1, 6))

# 4. random.randrange(start, stop, step) -> Like range(), stop is EXCLUSIVE
print("randrange(0, 10, 2):", random.randrange(0, 10, 2))  # Even numbers from 0 to 8

# 5. random.choice(seq) -> Picks ONE random element from a non-empty sequence (list, tuple, string)
fruits = ["apple", "banana", "mango", "orange"]
print("choice(fruits):", random.choice(fruits))

# 6. random.choices(population, k=n) -> Picks n elements WITH replacement (duplicates allowed)
print("choices(fruits, k=3):", random.choices(fruits, k=3))

# Weighted choices -> Give higher weights to items that should appear more often
print("choices with weights:", random.choices(["common", "rare"], weights=[90, 10], k=5))

# 7. random.sample(population, k=n) -> Picks n UNIQUE elements WITHOUT replacement (no duplicates)
numbers = [10, 20, 30, 40, 50]
print("sample(numbers, k=3):", random.sample(numbers, k=3))

# 8. random.shuffle(lst) -> Shuffles a mutable list IN PLACE (modifies original list, returns None)
cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print("shuffled cards:", cards)

# 9. random.seed(n) -> Fixes the random sequence so results are repeatable (great for debugging/testing)
random.seed(42)
print("seeded roll 1:", random.randint(1, 100))
random.seed(42)
print("seeded roll 2 (same):", random.randint(1, 100))
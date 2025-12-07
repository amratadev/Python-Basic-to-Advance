import random   # Import Python's random module

# 🎲 Dice roller → generates a random integer between 1 and 6
dice = random.randint(1, 6)
print("🎲 Dice rolled:", dice)

# 🔢 Random float → generates a random value between 0.0 and 1.0
print(random.random())

# 🎯 Random integer → generates a random integer between 0 and 9
print(random.randrange(10))

# 🎯 Random integer with step → generates a random integer from 0, 5, 10, or 15
print(random.randrange(0, 20, 5))

# 🎯 Random integer → generates a random integer between 10 and 19
print(random.randrange(10, 20))

# 🌊 Random float → generates a random float between 10 and 20
print(random.uniform(10, 20))

# 🎨 Random choice → selects a random element from the list
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))   # Example output: "green"

# 🃏 Shuffle → randomly reorders the elements in the list
cards = ["♠️ Ace", "♥️ King", "♦️ Queen", "♣️ Jack"]
random.shuffle(cards)
print("After shuffle:", cards)
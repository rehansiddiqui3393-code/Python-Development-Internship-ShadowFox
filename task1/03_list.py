# Section 3: List

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Original list:", justice_league)

# 1. Number of members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning (new leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:", justice_league)

# 4. Separate Aquaman and Flash using Green Lantern
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index + 1, "Green Lantern")
print("After separating Flash and Aquaman:", justice_league)

# 5. Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

# 6. Sort alphabetically
justice_league.sort()
print("Sorted team:", justice_league)
print("New leader:", justice_league[0])

# BONUS: Prediction -> "Cyborg" comes first alphabetically (C < G < H < M < S)

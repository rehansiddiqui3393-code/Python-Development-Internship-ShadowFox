# Section 5: For Loop
import random

# Q1: Dice simulation
rolls = 30
count_six = 0
count_one = 0
double_six = 0
previous = None
results = []

for _ in range(rolls):
    roll = random.randint(1, 6)
    results.append(roll)
    if roll == 6:
        count_six += 1
        if previous == 6:
            double_six += 1
    if roll == 1:
        count_one += 1
    previous = roll

print("Rolls:", results)
print("Times rolled a 6:", count_six)
print("Times rolled a 1:", count_one)
print("Times rolled two 6s in a row:", double_six)

# Q2: Jumping jacks workout
total = 100
done = 0
completed_all = True

for set_number in range(1, 11):
    done += 10
    print(f"Set {set_number} done. Jumping jacks completed: {done}")
    if done == total:
        break
    tired = input("Are you tired? (yes/y/no/n): ").strip().lower()
    if tired in ("yes", "y"):
        skip = input("Do you want to skip the remaining sets? (yes/y/no/n): ").strip().lower()
        if skip in ("yes", "y"):
            print(f"You completed a total of {done} jumping jacks.")
            completed_all = False
            break
    print(f"{total - done} jumping jacks are remaining.")

if completed_all:
    print("Congratulations! You completed the workout")

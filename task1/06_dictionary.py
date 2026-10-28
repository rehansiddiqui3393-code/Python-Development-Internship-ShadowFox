# Section 6: Dictionary

# Q1: Friends list and list of tuples
friends = ["Aditya", "Rahul", "Priya", "Sneha", "Karan", "Neha"]
friends_with_length = [(name, len(name)) for name in friends]
print("Friends:", friends)
print("Name with length:", friends_with_length)

# Q2: Trip expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())
print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

if your_total > partner_total:
    print("You spent more money overall")
elif partner_total > your_total:
    print("Your partner spent more money overall")
else:
    print("Both spent the same amount")

# Category with the biggest difference
max_category = None
max_diff = 0
for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        max_category = category

print(f"Biggest difference is in '{max_category}': {max_diff}")

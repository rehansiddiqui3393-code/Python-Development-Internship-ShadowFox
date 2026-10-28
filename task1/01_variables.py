# Section 1: Variables

# Q1: variable pi and its data type
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

# Q2: variable named 'for'
# for = 4  -> SyntaxError: invalid syntax
# Reason: 'for' is a reserved keyword in Python (used in loops),
# so it cannot be used as a variable name.
import keyword
print("Is 'for' a keyword?", keyword.iskeyword("for"))
for_value = 4
print("Valid alternative name, for_value =", for_value)

# Q3: Simple Interest = P x R x T / 100
principal = 10000
rate = 5
time = 3
simple_interest = (principal * rate * time) / 100
print("Simple Interest for 3 years:", simple_interest)

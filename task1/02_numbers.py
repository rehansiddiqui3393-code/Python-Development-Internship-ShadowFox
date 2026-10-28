# Section 2: Numbers

# Q1: format() with 145 and 'o'
def format_number(number, fmt):
    return format(number, fmt)

result = format_number(145, 'o')
print("format(145, 'o') =", result)
print("Representation used: Octal (base 8)")

# Q2: Area of circular pond
pi = 3.14
radius = 84
area = pi * radius ** 2
print("Area of pond:", area, "square meters")

# Bonus: water in pond (1.4 liters per square meter)
water = area * 1.4
print("Total water in pond (liters):", int(water))

# Q3: Speed in meters per second
distance = 490            # meters
time_seconds = 7 * 60     # 7 minutes in seconds
speed = distance / time_seconds
print("Speed (m/s):", int(speed))

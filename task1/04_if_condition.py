# Section 4: If Condition

# Q1: BMI Category
def bmi_category():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    bmi = weight / (height ** 2)
    print("Your BMI is:", round(bmi, 2))
    if bmi >= 30:
        print("Obesity")
    elif bmi >= 25:
        print("Overweight")
    elif bmi >= 18.5:
        print("Normal")
    else:
        print("Underweight")

# Cities by country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

def find_country(city):
    city = city.strip().title()
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    return None

# Q2: Which country does a city belong to
def city_country():
    city = input("Enter a city name: ")
    country = find_country(city)
    if country:
        print(f"{city.strip().title()} is in {country}")
    else:
        print("City not found in the list")

# Q3: Same country check
def same_country():
    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")
    c1 = find_country(city1)
    c2 = find_country(city2)
    if c1 is None or c2 is None:
        print("One or both cities are not in the list")
    elif c1 == c2:
        print(f"Both cities are in {c1}")
    else:
        print("They don't belong to the same country")

print("--- Q1: BMI ---")
bmi_category()
print("\n--- Q2: City to Country ---")
city_country()
print("\n--- Q3: Same Country ---")
same_country()

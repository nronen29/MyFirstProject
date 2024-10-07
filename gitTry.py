import math

def calculate_area(radius):
    """Calculate the area of a circle given the radius."""
    if radius <= 0:
        return "Radius must be greater than 0."
    area = math.pi * (radius ** 2)
    return area

if __name__ == "__main__":
    # Ask the user for the radius
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area(radius)
        print(f"The area of the circle with radius {radius} is {area:.2f}")
    except ValueError:
        print("Please enter a valid number.")
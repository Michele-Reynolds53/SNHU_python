cm_per_inch = 2.54
inches_per_foot = 12


def height_us_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters"""
    total_inches = feet * inches_per_foot + inches
    cm = total_inches * cm_per_inch
    return cm

feet = 6
inches = 4

centimeters = height_us_to_cm(feet, inches)
print(f'Centimeters: {centimeters}')

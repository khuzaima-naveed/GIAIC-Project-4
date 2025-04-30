# Constants for gravity ratios relative to Earth
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # User se Earth par wazan lena
    earth_weight = float(input("Enter a weight on Earth: "))

    # User se planet ka naam lena
    planet = input("Enter a planet: ")

    # Planet ke mutabiq gravity constant set karna
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        # Baaki case mein assume kar rahe hain ke Neptune hi hoga
        gravity_constant = NEPTUNE_GRAVITY

    # Wazan calculate karna aur round karna
    planetary_weight = earth_weight * gravity_constant
    rounded_weight = round(planetary_weight, 2)

    # Result print karna
    print("The equivalent weight on " + planet + ": " + str(rounded_weight))

# Program ko run karne ke liye
if __name__ == "__main__":
    main()

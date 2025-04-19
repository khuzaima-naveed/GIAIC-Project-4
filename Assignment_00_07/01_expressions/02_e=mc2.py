C: int = 299792458  # The speed of light in m/s

def main():
    mass_in_kg: float = float(input("\033[1;3mEnter kilos of mass: "))

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("\033[0me = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(energy_in_joules) + " joules of energy!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
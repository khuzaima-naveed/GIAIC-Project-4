def main():
    print("🚀 Welcome to the Space Adventure Mad Lib!\n")

    astronaut = input("Enter a name: ")
    planet = input("Enter a planet name: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    number = input("Enter a number: ")

    story = f"""
    Captain {astronaut} was on a mission to explore the planet {planet}.
    The surface was {adjective} and full of {noun}s.
    After {number} hours, the mission was a success and they returned to Earth as a hero!
    """

    print("\n🪐 Here's your Mad Lib story:\n")
    print(story)

if __name__ == "__main__":
    main()

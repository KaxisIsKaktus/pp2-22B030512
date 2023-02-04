print("Welcome to the Avatar Identifier for The Last Airbender!")
print("Please answer the following questions to determine your avatar.")

element = input("What is your elemental bending ability (Water, Earth, Fire, Air)? ")
nation = input("Which nation do you belong to (Water Tribe, Earth Kingdom, Fire Nation, Air Nomads)? ")

if element == "Water":
    if nation == "Water Tribe":
        print("You are Katara of the Southern Water Tribe!")
    else:
        print("You are Hama of the Northern Water Tribe!")
elif element == "Earth":
    print("You are Toph Beifong of the Earth Kingdom!")
elif element == "Fire":
    print("You are Azula of the Fire Nation!")
elif element == "Air":
    print("You are Aang of the Air Nomads!")
else:
    print("Invalid input. Please try again.")
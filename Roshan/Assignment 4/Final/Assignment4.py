# Program Code Starts Here
# Main Function 
def main():
    # To Call other functions and get user input
    displayInstructions()
    displayRaceOptions()
    # To get user input
    while True:
        #Checking for valid input
        raceChoice = int(input("Enter choice (1 - 9): "))
        if 0 < raceChoice < 10:
            #breaking the loop if the input is valid
            break
        print("Invalid choice. Please choose again...")
    displayClassOptions()
    # To get user input
    while True:
        #Checking for valid input
        classChoice = int(input("Enter choice (1 - 9): "))
        if 0 < classChoice < 10:
            #breaking the loop if the input is valid
            break
        print("Invalid choice. Please choose again...")
    # To get user input for choosing Race
    # To get user input for choosing Class
    # To call function determineRace
    _race = determineRace(raceChoice)
    # To call function determineClass
    _class = determineClass(classChoice)
    # To call function displayCharacters
    displayCharacter(_race, _class)


# Function to display instructions
def displayInstructions():
    # To display instructions
    print("Name, Races, Class taken From:")
    print("https://raw.githubusercontent.com/janelleshane/DnD-characters/master/DnD_characters_May2018.txt")
    print()
    print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
    print()
    print()
    print(" ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___")
    print("|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("|_|                                                       |_|")
    print("|_|                        WELCOME                        |_|")
    print("|_|_ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ _|_|")
    print("|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("|_|                                                       |_|")
    print("|_|        This name generator will give                  |_|")
    print("|_|        you  names suggestion based on                 |_|")
    print("|_|        a character's RACE and CLASS!                  |_|")
    print("|_|_ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ _|_|")
    print("|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print()
    print()
    print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
    print()
    print()


# Function displayRaceOptions
def displayRaceOptions():
    # To display
    print("====================")
    print("   Race Options  ")
    print("====================")
    print("   1. Human")
    print("   2. Elf")
    print("   3. Tiefling")
    print("   4. Gnome")
    print("   5. Goblin")
    print("   6. Dragonborn")
    print("   7. Half-Elf")
    print("   8. Orc")
    print("   9. Dwarf")
    print()


# Function displayClassOptions
def displayClassOptions():
    # To display
    print("====================")
    print("   Class Options  ")
    print("====================")
    print("   1. Cleric")
    print("   2. Druid")
    print("   3. Wizard")
    print("   4. paladin")
    print("   5. Bard")
    print("   6. Rogue")
    print("   7. Ranger")
    print("   8. Fighter")
    print("   9. Barbarian")
    print()


# Function determineRace
def determineRace(raceChoice):
    #List of Races 
    races = [
        'Human',
        'Elf',
        'Tiefling',
        'Gnome',
        'Goblin',
        'Dragonborn',
        'Halfling',
        'Orc',
        'Dwarf'
    ]
    # Return corresponding value
    return races[raceChoice - 1]


# Function determineClass
def determineClass(classChoice):
    classes = [
        "Cleric",
        "Druid",
        "Wizard",
        "Paladin",
        "Bard",
        "Rogue",
        "Ranger",
        "Fighter",
        "Barbarian"
    ]
    return classes[classChoice - 1]


# Function displayCharacter to display the character details
def displayCharacter(raceName, className):
    names = []
    namelist = []
    print("\n><><><><><><><><><><><><><><><><><><><><><><><\n")
    name = f" {raceName} / {className} Names "
    print('=' * len(name))
    print(name)
    print('=' * len(name))
    file = open("characters.txt", 'r')
    for lines in file:
        name = lines.strip().split(',')
        names.append(name)
    for i in range(len(names)):
        if [raceName, className] == names[i][1::]:
            namelist.append(i)
    if len(namelist) < 1:
        print("- No Names Found.")
    else:
        for j in namelist:
            print('-', names[j][0])
    print("\n><><><><><><><><><><><><><><><><><><><><><><><")



main()

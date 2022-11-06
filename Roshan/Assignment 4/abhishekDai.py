def main():
    displayInstructions()
    
    # Following 2 loops make sure user enters a valid option
    displayRaceOptions()
    while True:
        race = int(input("Enter choice (1 - 9): "))
        if 0 < race < 10:
            break
        print("Invalid choice. Please choose again....")

    displayClassOptions()
    while True:
        char_class = int(input("Enter choice (1 - 9): "))
        if 0 < char_class < 10:
            break
        print("Invalid choice. Please choose again....")

    # Retriving race and class names based on users input
    raceName = determineRace(race)
    className = determineClass(char_class)

    # Dislpaying available character names
    displayCharacters(raceName, className)


def displayInstructions():
    """ 
    This function prints the instuction for user in a formatted manner 
    """


    instructions = """
    Names, Races, Classes taken form:
      https://raw.githubusercontent.com/janelleshane/
      DnD-characters/master/DnD_characters_May2018.txt

    ><><><><><><><><><><><><><><><><><><><><><><><
       ____ ____ ____ ____ ____ ____ ____ ____  
      |____|____|____|____|____|____|____|____|
      |__|                                 |__|
      |__|            WELCOME!!            |__|
      |__|____ ____ ____ ____ ____ ____ ___|__| 
      |____|____|____|____|____|____|____|____|
      |__|                                 |__|
      |__|  This name generator will give  |__|
      |__|  you name suggestions based on  |__| 
      |__|  a character's RACE and CLASS   |__|
      |__|____ ____ ____ ____ ____ ____ ___|__| 
      |____|____|____|____|____|____|____|____|

    ><><><><><><><><><><><><><><><><><><><><><><><
    """
    print(instructions)


def displayRaceOptions():
    """
    This function displays the available races for user in a formatted manner
    """ 


    options = """
    ==============
    RACE OPTIONS
    ==============
    1. Human
    2. Elf
    3. Tiefling
    4. Gnome
    5. Goblin
    6. Dragonborn
    7. Halfling
    8. Orc
    9. Dwarf
    """
    print(options)


def displayClassOptions():
    """
    This function displays the available classes for user in a formatted manner
    """


    options = """
    ==============
    CLASS OPTIONS
    ==============
    1. Cleric
    2. Druid
    3. Wizard   
    4. Paladin
    5. Brag
    6. Rogue
    7. Ranger
    8. Fighter
    9. Barbarian
    """
    print(options)


def determineRace(race: int):
    """
    This function return the name of race chosen by the user
    """


    allRaces = ["Human", "Elf", "Tiefling", "Gnome",
                "Goblin", "Dragonborn", "Halfling", "Orc", "Dwarf"]
    return allRaces[race-1]


def determineClass(charClass: int):
    """
    This function return the name of class chosen by the user
    """


    allClasses = ["Cleric", "Druid", "Wizard", "Paladin",
                  "Brag", "Rogue", "Ranger", "Fighter", "Barbarian"]
    return allClasses[charClass-1]


def displayCharacters(raceName: str, className: str):
    """
    This function finds the available names based on users choice
    from the names file and displays it in a formatted manner
    """

    line = "><><><><><><><><><><><><><><><><><><><><><><><"
    title = f" {raceName}/{className} Names "
    print(line, "\n\n", "="*len(title), "\n",
          title, "\n", "="*len(title), "\n")

    # list to store names of available characters
    allNames = []

    with open("characters.txt", encoding = 'cp850') as f:    
        f.readline() # skipping the first line
        for i in range(364):
            info = f.readline()[:-1].split(",") # breaking the sentence into [name, race, class] format
            if info[1].lower() == raceName.lower() and info[2].lower() == className.lower(): # checking if the race and class matches
                allNames.append(info[0])

    for name in allNames:
        print(f"  - {name}")
    if len(allNames) == 0:  # just in case no names are round the following message is to be shown
        print("  - No Names Found")  

    print("\n", line)


main()  # calling the main function to start the function
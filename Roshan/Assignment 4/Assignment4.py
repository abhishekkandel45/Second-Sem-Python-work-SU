



# Program Code Starts Here
# Main Function 
def main():
#To Call other functions and get user input
    displayInstructions()
    displayRaceOptions()
    displayClassOptions()
    determineRace()
    determineClass()
    displayCharacters()
    #To get user input for choosing Race
    raceChoice = int(input())
    #To get user input for choosing Class
    classChoice = int(input())
    #To call function determineRace
    determineRace(raceChoice)
    #To call function determineClass
    determineClass(classChoice)
    #To call function displayCharacters
    displayCharacters(raceChoice,classChoice)



# Function to display instructions
def displayInstructions():
#To display instructions
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
    print("|_|        you  names suggesion based on                  |_|")
    print("|_|        a character's RAce and CLASS!                  |_|")
    print("|_|_ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ _|_|")
    print("|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print()
    print()
    print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
    print()
    print()

# Function displayRaceOptions
def displayRaceOptions():
#To display
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
    print("Enter your choice (1-9): ", end="")

# Function displayClassOptions
def displayClassOptions():
#To display
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
    print("Enter your choice (1-9): ", end="")

# Function determineRace
def determineRace(raceChoice):
    #To get user input for choosing
    raceChoice = int(input())
    # Validating user input from 1 to 9
    if raceChoice < 1 or raceChoice > 9:
        print("Invalid choice. Please try again.")
        determineRace()
    else:
        #To open file
        infile = open("characters.txt", "r")
        #To read file
        line = infile.readline()
        #To read line by line
        while line != "":
            #To split the line
            line = line.split(",")
            #To get the Race from the file and compare with user input cases as per Input
            if raceChoice == 1:
                if line[1] == "Human":
                    #To get the Name from the file
                    name = line[0]

            elif raceChoice == 2:
                if line[1] == "Elf":
                    #To get the Name from the file
                    name = line[0]

            elif raceChoice == 3:
                if line[1] == "Tiefling":
                    #To get the Name from the file
                    name = line[0]

            elif raceChoice == 4:
                if line[1] == "Gnome":
                    #To get the Name from the file
                    name = line[0]

            elif raceChoice == 5:
                if line[1] == "Goblin":
                    #To get the Name from the file
                    name = line[0]

            elif raceChoice == 6:
                if line[1] == "Dragonborn":
                    #To get the Name from the file
                    name = line[0]

            elif raceChoice == 7:
                if line[1] == "Half-Elf":
                    #To get the Name from the file
                    name = line[0]

            elif raceChoice == 8:
                if line[1] == "Orc":
                    #To get the Name from the file
                    name = line[0]

            elif raceChoice == 9:
                if line[1] == "Dwarf":
                    #To get the Name from the file
                    name = line[0]

            #To read next line
            line = infile.readline()
        #To close file
        infile.close()
        #To return name
        return name


# Function determineClass
def determineClass(classChoice):
    #TO get user input for choosing
    classChoice = int(input())
    # Validating user input from 1 to 9
    if classChoice < 1 or classChoice > 9:
        print("Invalid choice. Please try again.")
        determineClass()
    else:
        #To open file
        infile = open("characters.txt", "r")
        #To read file
        line = infile.readline()
        #To read line by line
        while line != "":
            #To split the line
            line = line.split(",")
            #To get the Class from the file and compare with user input cases as per Input
            if classChoice == 1:
                if line[2] == "Cleric":
                    #To get the Name from the file
                    name = line[0]

            elif classChoice == 2:
                if line[2] == "Druid":
                    #To get the Name from the file
                    name = line[0]

            elif classChoice == 3:
                if line[2] == "Wizard":
                    #To get the Name from the file
                    name = line[0]

            elif classChoice == 4:
                if line[2] == "Paladin":
                    #To get the Name from the file
                    name = line[0]

            elif classChoice == 5:
                if line[2] == "Bard":
                    #To get the Name from the file
                    name = line[0]

            elif classChoice == 6:
                if line[2] == "Rogue":
                    #To get the Name from the file
                    name = line[0]

            elif classChoice == 7:
                if line[2] == "Ranger":
                    #To get the Name from the file
                    name = line[0]

            elif classChoice == 8:
                if line[2] == "Fighter":
                    #To get the Name from the file
                    name = line[0]

            elif classChoice == 9:
                if line[2] == "Barbarian":
                    #To get the Name from the file
                    name = line[0]

            #To read next line
            line = infile.readline()
        #To close file
        infile.close()
        #To return name
        return name

# Function displayCharacter to display the character details
def displayCharacter(raceChoice, classChoice):
    #To display
    print()
    print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
    print()
    print("============================================")
    #printinning the character details
    print(determineRace(raceChoice), "/", determineClass(classChoice), "Names")
    print("============================================")
    #if race and class belongs to same category then print character
    if determineRace(raceChoice) == determineClass(classChoice):
        print("- ", determineRace(raceChoice));
        exit()
    else:
        print("-No Names Found-")
    print()    
    print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")






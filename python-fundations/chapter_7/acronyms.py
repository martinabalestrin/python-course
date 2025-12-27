def find_acronym():
    # Ask the user what acronym they want to look up
    look_up = input("What software acronym would you like to look up?\n")

    found = False

    try:
        # Open the file
        with open('python-fundations/chapter_7/input.txt') as file:
            for line in file:
                # Checks substrings in a string
                if look_up in line:
                    print(line)
                    found = True
                    break
                
    except FileNotFoundError as e:
        print('File not found')
        return

    if not found:
        print('The acronym does not exist')

def add_acronym():
    # Ask the user what acronym they want to add
    acronym = input("What acronym would you like to add?\n")

    # Then ask the user the definition
    definition = input("What is the definition?\n")

    # Open the file
    with open('python-fundations/chapter_7/input.txt', 'a') as file:
        # 'a' opens the file for appending!
        
        # Write the new acronym and definition to the file
        file.write(acronym + ' - ' + definition + '\n')

def main():
    # Ask the user whether they want to find or add an acronym
    choice = input('Do you want to find(F) or add(A) an acronym?\n')

    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()
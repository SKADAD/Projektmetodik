import model.DungeonMap
# import os


class AccountManager:

    def __init__(self):
        # self.character() # TODO
        self.character_hero = "Hero Type"
        self.character_name = "Nam!e"
        self.starting_pos = "NW"
        self.size_of_map = 1

    # First game menu and choices, validates input and finally calls for the next function
    def start_menu(self):
        # Number of choices in the menu
        max_value_for_menu = 2
        # Clears the terminal:
        clear_cmd()
        print("Enter choice:\n 1. New Character \n 2. Existing Character\n")
        # Returns true if choice is valid
        choice = choice_validate_int(max_value_for_menu)
        if not choice:
            # Returns to start of this menu
            self.start_menu()
        # If the return is valid
        elif choice:
            # If user selected 1
            if user_input_number == 1:
                # Sends the user to menu create new char
                self.menu_char_new()
            # If user selected 2
            elif user_input_number == 2:
                # Sends the user to menu load existing
                self.menu_char_existing()

    # Create new character intro and finally calls new player name
    def menu_char_new(self):
        clear_cmd()
        max_value_of_menu = 3
        print("Choose hero by number:\n 1. Warrior\n 2. Wizard\n 3. Thief\n")
        choice = choice_validate_int(max_value_of_menu)
        if not choice:
            print("Invalid choice")
            self.menu_char_new()
        elif choice:
            if user_input_number == 1:
                self.character_hero = "Warrior"
            elif user_input_number == 2:
                self.character_hero = "Wizard"
            elif user_input_number == 3:
                self.character_hero = "Thief"
            else:
                print("Unexpected.")
            # Sends the user to next menu
            self.menu_new_player_name()
        else:
            print("Unexpected..")

    # Create new name for new character and starts map
    def menu_new_player_name(self):
        choice = str(input("Enter a character name:\n"))
        # TODO check if user name already exists
        # TODO save character to account
        self.character_name = choice
        print("Your new name is: " + self.character_name)
        self.menu_map_size()

    # User selects map size and set position function starts
    def menu_map_size(self):
        clear_cmd()
        max_value_of_menu = 3
        print("Select map size:\n 1. 16 rooms\n 2. 25 rooms \n 3. 64 rooms\n")
        choice = choice_validate_int(max_value_of_menu)
        if not choice:
            clear_cmd()
            self.menu_map_size()
        elif choice:
            if user_input_number == 1:
                print("Choice =4")
                self.size_of_map = 4
            elif user_input_number == 2:
                self.size_of_map = 5
            elif user_input_number == 3:
                print("Choice =8")
                self.size_of_map = 8
            self.menu_player_position()

    # Position is selected. The end is todo:
    def menu_player_position(self):
        clear_cmd()
        max_value_of_menu = 4
        print("Enter starting position:\n 1. North West\n 2. North East\n 3. South West\n 4. South East\n")
        choice = choice_validate_int(max_value_of_menu)
        if not choice:
            self.menu_player_position()
        elif choice:
            if user_input_number == 1:
                self.starting_pos = "NW"
            elif user_input_number == 2:
                self.starting_pos = "NE"
            elif user_input_number == 3:
                self.starting_pos = "SW"
            elif user_input_number == 4:
                self.starting_pos = "SE"
            else:
                print("Unexpected, selecting default:" + self.starting_pos)
            self.present_result()
        # TODO send character data from here
        else:
            print("Unexpected2")

    # Prints the choices made in menu:
    def present_result(self):
        print("Name: " + self.character_name)
        print("Hero Class: " + self.character_hero)
        print("Map Total Rooms: " + str(self.size_of_map * self.size_of_map))
        print("Map starting position: " + self.starting_pos)

    # Load existing character
    def menu_char_existing(self):
        # TODO Look if char exists and if so load:
        clear_cmd()
        print("Choice 2, trying to load existing char..")


# Clear CLI / GUI from lines when needed
def clear_cmd():
    try:
        print("\n\n\n\n")
    # disabled (debug mode on)
    # os.system('CLR')
    # os.system('clear')
    except:
        print("Tried to clear CLI but failed")


# Validates the users input when called
def choice_validate_int(highest_value_in_menu):
    # This global variable remembers the users selected number for menu if choice_validate first confirms True
    global user_input_number
    try:
        user_choice = int(input(""))
        # Choices in a menu is at minimum 1 and up to or as <number defined in the call to this function>
        if not (1 <= user_choice <= highest_value_in_menu):
            raise ValueError()
        else:
            # Else remember the number chosen (int)
            user_input_number = user_choice
            return True
    except ValueError:
        return False


start = AccountManager()
start.start_menu()
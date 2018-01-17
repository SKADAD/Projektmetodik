import random
from model.Player import Player
from model.Statistics import Statistics


class CombatController:

    def __init__(self, controller, list_of_monsters):
        self.controller = controller
        self.player = controller.character
        self.order_of_attack = []
        self.list_of_monsters = list_of_monsters
        # self.list_of_monsters = []

    def start(self):
        #Skapa ordningen. Så länge det finns minst ett monster i listan över monster och spelaren lever så får spelaren ett val medan monster attakerar
        self.create_order_of_attack()
        while len(self.list_of_monsters) > 0 and self.player.is_alive:
            for creature in self.order_of_attack:
                if type(creature) is Player:
                    action = self.player_action()
                    if action == "flee":
                        return
                else:
                    self.monster_attack(creature)

    def player_action(self):
        # Se till att det är ett korrekt värde från spelaren. Lista igenom monster med deras index +1 först.
        # Konvertera input till int. Antingen fly, eller attackera valt monster.

        while True:
            self.controller.to_print("Choose your action:")
            for i, monster in enumerate(self.list_of_monsters):
                self.controller.to_print(str(i + 1) + ". Attack the " + monster.short_string())
            self.controller.to_print("0. Flee to the previous room")

            try:
                choice = int(input())
            except ValueError:
                self.controller.to_print("Must enter a valid input!")
                continue

            if choice == 0:
                if self.flee():
                    print("You fled from the room!")
                    return "flee"
                else:
                    print("Your escape attempt failed!")
                    return "failed"
            elif choice <= len(self.list_of_monsters):
                self.player_attack(self.list_of_monsters[choice - 1])
                return "attack"
            else:
                self.controller.to_print("Must enter a valid input!")

    def create_order_of_attack(self):
        # Skapa en dictionary med varje deltagare och deras initiativ för striden.
        # Skapa en sorterad lista med det rullade initiativet som sorteringsvärde. Reverse=True ger högst först.

        dict_of_initiative = {self.player: self.roll_dice(self.player.initiative)}
        for monster in self.list_of_monsters:
            dict_of_initiative[monster] = self.roll_dice(monster.initiative)

        sorted_list_of_initiative = sorted(dict_of_initiative, key=dict_of_initiative.get, reverse=True)
        for creature in sorted_list_of_initiative:
            self.order_of_attack.append(creature)

    @staticmethod
    def roll_dice(number_of_dices):
        value = 0
        for i in range(number_of_dices):
            value += random.randint(1, 6)
        return value

    def player_attack(self, monster_target):
        player_attack = self.roll_dice(self.player.attack)
        enemy_agility = self.roll_dice(monster_target.agility)
        if player_attack >= enemy_agility:
            print("Attack hit " + monster_target.monster_type + " for 1 durability.")
            monster_target.durability -= 1
            if monster_target.durability <= 0:
                print(monster_target.monster_type + " died!")
                Statistics.monster_killed(monster_target.monster_type)
                self.list_of_monsters.remove(monster_target)
        else:
            print("Your attack missed")

    def monster_attack(self, monster):
        monster_attack = self.roll_dice(monster.attack)
        player_agility = self.roll_dice(self.player.agility)
        if monster_attack > player_agility:
            print(monster.monster_type + " hit you for 1 durability.")
            self.player.durability -= 1
            if self.player.durability <= 0:
                self.player.is_alive = False
                print("Game over")
        else:
            print(monster.monster_type + " missed you.")

    def flee(self):
        flee_var = self.player.agility * 10
        dice_roll = random.randrange(0, 100)
        if dice_roll <= flee_var:
            self.controller.dungeon_map.playerPosX = self.controller.dungeon_map.last_position[0]
            self.controller.dungeon_map.playerPosY = self.controller.dungeon_map.last_position[1]
            return True
        else:
            return False



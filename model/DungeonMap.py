import random
import os, sys, time
sys.path.append('../')
from model.Room import Room
from Controller.Controller import *

class DungeonMap:

    room = Room

    def __init__(self, size_, start_position):
        self.list_of_rooms = []
        self.playerPosX = 0
        self.playerPosY = 0
        self.size = size_

        print("Generating starting pos..")
        self.generate_starting_pos(start_position)
        print("Generating rooms..")
        self.generate_rooms()
        #print("Generating exits..")
        #self.generate_exit()


    def generate_rooms(self):
        for i in range(self.size):
            self.list_of_rooms.append([])
            for j in range(self.size):
                room = Room()
                # If the position is the same as the starting position, set no monsters and no treasure
                if i == self.playerPosX and j == self.playerPosY:
                    room.list_of_monsters = []
                    room.list_of_treasure = []
                self.list_of_rooms[i].append(room)

    def generate_exit(self):
        # Generate a random index in list range. Set exit to true, no monsters and no treasure
        while True:
            int_x = random.randrange(0, self.size)
            int_y = random.randrange(0, self.size)
            if not self.playerPosX == int_x and self.playerPosY == int_x:
                break

        room = self.list_of_rooms[int_x][int_y]
        room.is_exit = True
        room.list_of_monsters = []
        room.list_of_treasure = []

    def generate_starting_pos(self, position):
        print("Starting function..")
        if position is "NW":
            print("If NW has been passed..")
            self.playerPosX = 0
            self.playerPosY = 0
            print("Player pos is added")
        elif position is "NE":
            self.playerPosX = self.size - 1
            self.playerPosY = 0
        elif position is "SW":
            self.playerPosX = 0
            self.playerPosY = self.size - 1
        elif position is "SE":
            self.playerPosX = self.size - 1
            self.playerPosY = self.size - 1


    def print_map(self):
        string_to_print = ""

        for row in range(len(self.list_of_rooms)):
            for element in range(len(self.list_of_rooms[row])):
                if self.playerPosX == row and self.playerPosY == element:
                    string_to_print += "P "
                    continue
                room = self.list_of_rooms[row][element]
                #room = Room()
                if room.visited_room:
                    string_to_print += "O "
                else:
                    string_to_print += "X "
            string_to_print += "\n"
        toPrint(string_to_print)





    def move_player(self, direction):
        print(self.playerPosX)
        print(self.playerPosY)
        time.sleep(1)
        if direction == "w":
            if self.playerPosX - 1 >= 0:
                self.playerPosX -= 1
        elif direction == "a":
            if self.playerPosY - 1 >= 0:
                self.playerPosY -= 1
        elif direction == "s":
            if self.playerPosX + 1 < self.size:
                self.playerPosX += 1
        elif direction == "d":
            if self.playerPosY + 1 < self.size:
                self.playerPosY += 1
        room = self.get_player_room()
        room.visited_room = True
        return room

    def get_player_room(self):
        return self.list_of_rooms[self.playerPosX][self.playerPosY]


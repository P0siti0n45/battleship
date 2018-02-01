"""Battleship game

Python TeamWork week 1 @ Codecool Budapest

made by: Tamás Petki
         Richárd Hriech

uploaded to Github
"""
import os
import time
import random
import sys


def fullscreen():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=1000, cols=1000))
    print(" ")


def zoom():
    try:
        os.system("xdotool key Ctrl+plus")
    except BaseException:
        pass


def default_zoom():
    try:
        os.system("xdotool key Ctrl+0")
    except BaseException:
        pass


def get_terminal_columns():
    columns = -1
    rows, columns = os.popen('stty size', 'r').read().split()

    return int(columns)


def loading():
    strings = []

    strings.append("""
    |=============================================|
    |#####                                        |
    |==================== 11% ====================|
                Loading Unreal Engine 4
    """)

    strings.append("""
    |=============================================|
    |################################             |
    |==================== 66% ====================|
                   Loading textures
    """)

    strings.append("""
    |=============================================|
    |#############################################|
    |==================== 100% ===================|

    """)

    os.system("clear")
    os.system("clear")
    for i in range(3):
        time.sleep(1.1)
        os.system("clear")
        print(strings[i])
        time.sleep(1.1)


def intro():
    """plays before starting the game"""
    l = []
    l.append(" ______     ______     ______   ______   __         ______     ______     __  __     __     ______  ")
    l.append("/\  == \   /\  __ \   /\__  _\ /\__  _\ /\ \       /\  ___\   /\  ___\   /\ \_\ \   /\ \   /\  == \ ")
    l.append("\ \  __<   \ \  __ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\   \ \___  \  \ \  __ \  \ \ \  \ \  __/ ")
    l.append(" \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\  \ \_\   ")
    l.append("  \/_____/   \/_/\/_/     \/_/     \/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/   \/_/   ")
    l.append("                                                                                                    ")
    l.append("                                                  # #  ( )                                          ")
    l.append("                                               ___#_#___|__                                         ")
    l.append("                                           _  |____________|  _                                     ")
    l.append("                                    _=====| | |            | | |==== _                              ")
    l.append("                              =====| |.---------------------------. | |====                         ")
    l.append("                <--------------------'   .  .  .  .  .  .  .  .   '--------------/                  ")
    l.append("                  \                                                             /                   ")
    l.append("                   \___________________________________________________________/                    ")
    l.append("               wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                ")
    l.append("             wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww               ")
    l.append("                wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                 ")
    for i in range(1, len(l[0]) + 1):  # fly in from left animation
        os.system("clear")
        for j in l:
            print(j[-i:])
            time.sleep(0.003)  # slowing down

    time.sleep(1)
    input("""
                      +-++-++-++-++-+ +-++-++-++-++-+ +-++-+ +-++-++-++-++-+
                      |P||R||E||S||S| |E||N||T||E||R| |T||O| |S||T||A||R||T|
                      +-++-++-++-++-+ +-++-++-++-++-+ +-++-+ +-++-++-++-++-+""")

    for i in range(len(l[0])):  # flying out to the left
        os.system("clear")
        for j in l:
            print(j[i:])
            time.sleep(0.003)


def generate_outro(winner):
    """generates text for the outro"""
    char_list = [" * ", '   ', '   ', '\033[93m * \033[0m',
                 '   ', '   ']  # elements of the stars pattern
    text = ""
    for i in range(6):  # 6 rows first
        for j in range(28):
            text += random.choice(char_list)  # printing a row of the pattern
        text += "\n"
    for j in range(11):  # half of a row
        text += random.choice(char_list)
    text += winner.upper() + " WINS!"  # inserting winners name in the middle
    for j in range(11):  # half of a row
        text += random.choice(char_list)
    text += "\n"
    for i in range(6):  # 6 rows after
        for j in range(28):
            text += random.choice(char_list)
        text += "\n"
    return text


winner = "test"


def outro():
    for i in range(30):
        os.system("clear")
        print(generate_outro(winner))
        time.sleep(0.2)


class Board():
    """This is the map itself.

    Both players will get an instance.

    Contains ship placements, a part of the game enginge and
    drawing the boards to the terminal.
    """

    def __init__(self):
        self.coords = []  # will be 2 dimensional below
        self.drawing = ""
        self.game_on = False
        self.hit = 0
        self.max_hits = 0
        self.name = ""
        self.ships_list = []

        for x in range(10):  # generating 2D array for the map
            self.coords.append([])
            for y in range(10):
                self.coords[x].append(0)

    def print_board(self):
        """Prints the board to the terminal

        It prints out one big string based on coordinates

        when the ship placement is done,
        game_on turns True and the printing changes
        """
        half_map = ""

        for i in range(get_terminal_columns()):
            half_map += " "

        half_map = half_map[:int(len(half_map) / 2) - 10]

        os.system("clear")  # clean start
        self.drawing = ""
        # prints out coordinate system numbers
        # ugly because of color codes
        self.drawing += half_map + \
            " \033[1;32m 0 1 2 3 4 5 6 7 8 9\033[1;m \033[1;31mx\033[1;m\n"
        for y in range(10):
            self.drawing += half_map + "\033[1;32m{0}\033[1;m".format(str(y))
            for x in range(10):
                # water
                if self.coords[x][y] == 0:
                    self.drawing += "░░"
                # ship
                elif self.coords[x][y] == 1 and self.game_on is False:
                    self.drawing += "██"
                # when game is on, ships are hidden
                elif self.coords[x][y] == 1 and self.game_on is True:
                    self.drawing += "░░"
                # hits are red
                elif self.coords[x][y] == 2 and self.game_on is True:
                    self.drawing += "\033[1;31m██\033[1;m"
                # missed hits are blue
                elif self.coords[x][y] == 3 and self.game_on is True:
                    self.drawing += "\033[1;44m░░\033[1;m"

            self.drawing += "\n"
        self.drawing += half_map + "\033[1;31my\033[1;m"
        print(self.drawing)

    def ship_placement(self):
        """At the beginning of the game,
        the players choose the coords of their ships
        """
        self.print_board()
        # first argument in range -> smallest ship
        # second argument minus one -> biggest ship
        # every for loop creates a new ship
        for length in range(2, 4):
            while True:
                try:
                    x, y, orientation = input(
                        "Enter coordinates and orientation "
                        "of ship {0}, e.g.: 2,3,v\n".format(length)).split(",")
                    x = int(x)
                    y = int(y)

                    # 3rd value should be v or h (vertical or horizontal)
                    if orientation != "v" and orientation != "h":
                        print("Not valid orientation!")
                        continue

                    # coords can't be negative
                    if x < 0 or y < 0:
                        print("Ship is out of map!")
                        continue

                    # ships can't be placed outside of the map
                    if orientation == "h" and x + length > 10:
                        print("Ship is out of map!")
                        continue

                    if orientation == "v" and y + length > 10:
                        print("Ship is out of map!")
                        continue

                    # players can't place ships where there's one already
                    if orientation == "h":
                        ok = True
                        for i in range(length):
                            if self.coords[x + i][y] == 1:
                                ok = False
                                break

                        if not ok:
                            print("There's already a ship placed there!")
                            continue
                    # same but vertically
                    if orientation == "v":
                        ok = True
                        for i in range(length):
                            if self.coords[x][y + i] == 1:
                                ok = False
                                break

                        if not ok:
                            print("There's already a ship placed there!")
                            continue

                except ValueError:  # if coords can't be converted to ints
                    print("Not valid coordinates")
                    continue
                break

            # if everything went alright set the coordinates of the ship
            if orientation == "v":
                for i in range(length):
                    self.coords[x][y + i] = 1
                    self.ships_list.append([x, y + i])

            if orientation == "h":
                for i in range(length):
                    self.coords[x + i][y] = 1

            self.max_hits += length

            self.print_board()
        self.print_board()

    def attack(self):
        """The other player attacks your board"""
        while True:
            try:
                fire_x, fire_y = input(
                    "Fire to X and Y coordinates: ").split(",")
                fire_x = int(fire_x)
                fire_y = int(fire_y)

                if fire_x < 0 or fire_y < 0:
                    print("Invalid input!")

            except ValueError:
                print("Invalid input!")
                continue

            if self.coords[fire_x][fire_y] == 1:
                self.coords[fire_x][fire_y] = 2
                self.hit += 1  # counting the successful hits

            elif self.coords[fire_x][fire_y] == 0:
                self.coords[fire_x][fire_y] = 3
            break


board1 = Board()
board2 = Board()

default_zoom()
for i in range(3):
    zoom()
fullscreen()
loading()
intro()
print(" ")

board1.name = input("Enter player 1's name: ")
board2.name = input("Enter player 2's name: ")

board1.ship_placement()
input("Press Enter to continue...")
board2.ship_placement()
input("Game starts...")

# initialize maps

board1.game_on = True
board2.game_on = True

winner = ""

# after setting up the boards, the game itself starts:
while board1.hit < 5 or board2.hit < 5:
    input("\033[1m{0}\033[0m's turn".format(board1.name))
    board2.print_board()
    board2.attack()
    if board2.hit == board2.max_hits:
        winner = board1.name
        break
    board2.print_board()
    input("\033[1m{0}\033[0m's turn".format(board2.name))
    board1.print_board()
    board1.attack()
    if board1.hit == board1.max_hits:
        winner = board2.name
        break
    board1.print_board()

outro()
# default_zoom()

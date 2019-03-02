"""---------------------
Lionell Carlo Paquit
IE Digital Code Challenge
-------------------------"""


class PacMan:
    # Define and initialise properties of the class
    def __init__(self):
        self.X = None
        self.Y = None
        self.F = None
        self.dim_X = 5
        self.dim_Y = 5
        self.dir = ["NORTH", "EAST", "SOUTH", "WEST"]

    # Function that checks whether the move or place of pacman is on or off grid.
    # Returns True if it is within the grid and False if it falls off the grid
    def check_grid(self, x, y):
        if 0 <= x < self.dim_X and 0 <= y < self.dim_Y:
            return True
        else:
            return False

    # Function for the PLACE command. Sets the position X, Y and direction.
    def place(self, param):
        x = int(param[0])
        y = int(param[1])
        if self.check_grid(x, y):
            self.X = x
            self.Y = y
            self.F = param[2].upper()
        else:
            print("X, Y exceeds the grid...")

    # Function that move pacman one unit if not exceeding the grid
    def move(self):
        x = self.X
        y = self.Y

        if self.F == "NORTH":
            y += 1
            if self.check_grid(x, y):
                self.Y = y
                print("Moving north...")
            else:
                print("Off grid not moving...")
        elif self.F == "SOUTH":
            y -= 1
            if self.check_grid(x, y):
                self.Y = y
                print("Moving south...")
            else:
                print("Off grid not moving...")
        elif self.F == "EAST":
            x += 1
            if self.check_grid(x, y):
                self.X = x
                print("Moving east...")
            else:
                print("Off grid not moving...")
        elif self.F == "WEST":
            x -= 1
            if self.check_grid(x, y):
                self.X = x
                print("Moving west...")
            else:
                print("Off grid not moving...")

    # Function that rotate the direction pacman facing to 90 degrees from it's initial direction
    def rotate(self, direction):
        if direction == "LEFT":
            print("Going left...")
            if self.F == "NORTH":
                self.F = "WEST"
            elif self.F == "WEST":
                self.F = "SOUTH"
            elif self.F == "SOUTH":
                self.F = "EAST"
            elif self.F == "EAST":
                self.F = "NORTH"
        elif direction == "RIGHT":
            print("Going right...")
            if self.F == "NORTH":
                self.F = "EAST"
            elif self.F == "EAST":
                self.F = "SOUTH"
            elif self.F == "SOUTH":
                self.F = "WEST"
            elif self.F == "WEST":
                self.F = "NORTH"

    # Function that prints the status of pacman (X, Y, F)
    def report(self):
        print("Output: %d,%d,%s" % (self.X, self.Y, self.F))


# Only run the main function if we execute directly on this file.
if __name__ == "__main__":

    # Read commands in the input file
    filename = "input.txt"
    line = open(filename).read().splitlines()
    Game = PacMan()

    for a in line:
        if a.__contains__("PLACE"):
            print("Place: " + a[6:])
            place_attr = a[6:].split(',')
            Game.place(place_attr)
        # Does not proceed if a PLACE was not initialise
        elif a is not '' and Game.X is not None and Game.Y is not None and Game.F is not None:
            if a.upper().__contains__("MOVE"):
                Game.move()
            elif a.upper().__contains__("LEFT") or a.upper().__contains__("RIGHT"):
                Game.rotate(a.upper())
            elif a.upper().__contains__("REPORT"):
                Game.report()
            else:
                print("Command " + a + " is an invalid command.")
class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        self.swap_item() # Initially swap first item for default "none"
        while True:
            if not self.can_move_right(): # if you can't move right, the list must be only one item long, swap item back
                # to 'none' and end loop
                self.swap_item()
                break
            while self.can_move_right(): # if you can move right, there must be items to compare against, so move right
                self.move_right()
                if self.compare_item() == 1: # compare items, if item you hold is greater, swap
                    self.swap_item()
            while self.can_move_left() and self.compare_item() is not None: # at end of list, if you can move left, keep
                # moving left, stopping at "none"
                self.move_left()
            self.swap_item() # swapping with none and dropping smallest value
            self.move_right() # move right so everything to left of "none" is sorted
            self.swap_item() # dropping none for next unsorted value and continuing on

        # # checks to see if you can move left, if yes, you will move. if not, you will stay there.
        # self.light_is_on()
        # while self.light_is_on() is True:
        #     while self.can_move_left() is True:
        #         self.move_left()
        #         # turning the light off to begin:
        #     self.set_light_off()
        #     # checking to see if we can move right:
        #     while self.can_move_right() is True:
        #         # if we are able to move right, we are not at the end of the list, so we are going to sort:
        #         # PICKS UP ITEM
        #         self.swap_item()
        #         # MOVES TO NEXT ITEM
        #         self.move_right()
        #         # COMPARES/ SORTS THE TWO ITEMS
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             # Sets light on
        #             self.set_light_on()
        #         # move Left to put item back down
        #         self.move_left()
        #         # put the item back down where we got it from
        #         self.swap_item()
        #         self.move_right()
        # Any time any object gets swapped, we will turn the light on:
        # once can_move_right returns false, we are at the end of the list. Here is where we check to see if the
        # light has been turned on

    # move all the way left [x]
    # turn off light [x]
    # move right [x]
    # sort/take/swap [x]
    # turn light on if you swap/sort/take [x]
    # hit the end of the list, if the light is on, start over. [x]

    if __name__ == "__main__":
        # Test our your implementation from the command line
        # with `python robot_sort.py`

        l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94,
             99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85,
             27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63,
             31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

        robot = SortingRobot(l)

        robot.sort()
        print(robot._list)


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
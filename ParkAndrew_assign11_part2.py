"""
Assignment #11, Part 2
Andrew Park
"""

import random


class Gumball_Machine:
    def __init__(self, capacity):
        self.capacity = capacity
        # instance variables money to keep track of how much money is in the machine
        self.money = 0
        # a list to hold that many gumballs
        self.gumballs = []
        # local list holding color
        color = ["red", "green", "blue"]
        # iterate till the capacity
        for index in range(self.capacity):
            # generate random number
            selectedColor = random.randint(0, 2)
            # adding color to gumball list
            self.gumballs.append(color[selectedColor])
        # The constructor should 'announce' that it was constructed with the desired capacity
        print("Gumball Machine created with {} random gumballs".format(self.capacity))

    def report(self):
        # print the capacity and money
        print("\nGumball Machine Report:")
        print("* Gumballs in machine: {}".format(len(self.gumballs)))
        print("* Money in machine: ${:.2f}".format(self.money))

    def dispense(self, coin):
        # if the coin value is 0.25 and there is gumball left in the machine
        if coin == 0.25 and len(self.gumballs) > 0:
            # remove the gumball from the list
            print("\nAccepting {}; Dispensing a {} gumball".format(coin, self.gumballs.pop()))
            # increment the money value by adding the coin value to it
            self.money += coin
        # if the entered coin value is not quarter
        elif coin != 0.25:
            print("\nInvalid coin, no gumball will be dispensed")
        # if machine emptys
        else:
            print("\nMachine is empty, no gumball will be dispensed")

    def count_gumballs_by_type(self, gumball):
        print("\nThere are {} gumballs of type {} in the machine".format(self.gumballs.count(gumball), gumball))


def main():
    # create gumball of capacity 5
    machine = Gumball_Machine(5)
    machine.report()
    # call count_gumballs_by_type with different colors to know how many left
    machine.count_gumballs_by_type("red")
    machine.count_gumballs_by_type("green")
    machine.count_gumballs_by_type("blue")

    machine.dispense(0.10)
    machine.dispense(0.50)
    machine.dispense(0.01)

    machine.report()

    machine.count_gumballs_by_type("red")
    machine.count_gumballs_by_type("green")
    machine.count_gumballs_by_type("blue")

    machine.dispense(0.25)
    machine.dispense(0.25)
    machine.dispense(0.25)

    machine.report()

    machine.count_gumballs_by_type("red")
    machine.count_gumballs_by_type("green")
    machine.count_gumballs_by_type("blue")

    machine.dispense(0.25)
    machine.dispense(0.25)
    machine.dispense(0.25)

    machine.report()

    machine.count_gumballs_by_type("red")
    machine.count_gumballs_by_type("green")
    machine.count_gumballs_by_type("blue")


if __name__ == "__main__":
    # calling main function
    main()
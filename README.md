In this program you will be writing a class to simulate a "gumball machine" that you would see at a store. Your class should work as follows:
  - Constructor
    - The constructor should accept a capacity for the gumball machine (how many gumballs it is filled with - an integer). The gumball machine should store this capacity as an instance variable. No data validation is required.
    - The constructor should also store an instance variable to keep track of how much money is in the machine. All machines are constructed to be empty and have no money in them.
    - The constructor should also create a new instance variable (a list) to hold that many gumballs. Fill this list with a random set of gumballs - each gumball can be either red, green or blue.
    - The constructor should 'announce' that it was constructed with the desired capacity
  - Methods
    - report: this method should accept no arguments and simply report out the current status of the gumball machine.
    - dispense: this method should accept an argument - a coin value - and determine if that coin value is a quarter (i.e. 0.25). If so, a gumball should be removed from the the list and reported to the user. The machine should also accept the coin and increase its internal count of how much money is in the machine. Note that if the gumball machine is empty a new gumball will not be dispensed, and the coin should be rejected.
    - count_gumballs_by_type: this method should accept a single argument - a string representing the type of gumball - and print out how many types of that gumball are left in the machine.

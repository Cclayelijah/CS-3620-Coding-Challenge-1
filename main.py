
def getInterest():
    p = input('Principle: ')
    n = input('Number of years: ')
    r = input('Rate of interest: ')
    return int(p) * int(n) * int(r) / 100

def displaySquareValues():
    for x in range(1,10):
        print(x * x)

if __name__ == '__main__':
    # part 1
    interestValue = getInterest()
    print("Total Interest = " + str(interestValue))

    # part 2
    favoriteFood = ["Pizza", "Hot Pot", "Fruit", "Chips", "Dim Sum"]
    print("One of my favorite foods of all time is " + favoriteFood[2])
    favoriteFood.append("Salsa and Chips")
    favoriteFood.append("Fried Chicken")
    print("My list includes: " + str(favoriteFood))
    favoriteFood.insert(2, "Tacos")
    print("Now it is: " + str(favoriteFood))

    # part 3
    for x in range(5):
        print("I am a programmer")
    displaySquareValues()


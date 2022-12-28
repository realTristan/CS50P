# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Guessing Game          //
# //                                    //
# ////////////////////////////////////////
import random

# // Get the level of the guessing game
level: int = -1
while level < 0:
    try:
        level = int(input("Level: "))
    except Exception:
        pass


# // Generate a random number and set
# // the current guess to a negative
rand_num: int = random.randint(0, level)
guess: int = -1

# // While the guess is incorrect...
while 1:
    try:
        # // Get the users guess
        guess: int = int(input("Guess: "))

        # // If valid guess
        if guess > 0 and guess < level:

            # // Print guess proximity
            if guess < rand_num:
                print("Too small!")

            elif guess > rand_num:
                print("Too large!")

            elif guess == rand_num:
                print("Just right!")
                break

    # // If an error occurs, ignore it
    except Exception:
        pass

# check50 cs50/problems/2022/python/game
# submit50 cs50/problems/2022/python/game
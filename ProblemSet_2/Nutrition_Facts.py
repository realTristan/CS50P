# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Nutrition Facts        //
# //                                    //
# ////////////////////////////////////////

# // Store the nutrition facts in a dictionary
facts: dict[str, int] = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50
}

# // Get the inputted fruit
fruit: str = input("Item: ").lower()

# // If the fruit is in the nutrition facts map
if fruit in facts:
    # // Print the it's calories
    print(f"Calories: {facts[fruit]}")
    
# check50 cs50/problems/2022/python/nutrition
# submit50 cs50/problems/2022/python/nutrition
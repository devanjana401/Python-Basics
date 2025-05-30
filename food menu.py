pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}
recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
     "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}
for i in range(5):
    print("Recipes:")
    for r in recipes:
        print("-", r)
    # if choice in recipes:
    #     can_cook = True
    #     for item in recipes[choice]:
    #         if item not in pantry or pantry[item] < 1:
    #             print("You don't have enough", item)
    #             can_cook = False
    #             break

    #     if can_cook:
    #         for item in recipes[choice]:
    #             pantry[item] -= 1
    #         print("Cooked", choice)
    #     else:
    #         print("Can't cook", choice)
    # else:
    #     print("Recipe not found.")

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
for _ in range(3):  # You can change 3 to how many times you want to allow cooking
    print("\nAvailable Recipes:")
    for i, recipe in enumerate(recipes.keys(), 1):
        print(f"{i}. {recipe}")
    choice = int(input("Enter the number of the recipe you want to cook: "))
    selected_recipe = list(recipes.keys())[choice - 1]
    ingredients = recipes[selected_recipe]
    can_cook = True
    for item in ingredients:
        if pantry.get(item, 0) < 1:
            print(f"Cannot cook {selected_recipe}. Missing or insufficient: {item}")
            can_cook = False
            break
    if can_cook:
        for item in ingredients:
            pantry[item] -= 1
        print(f"{selected_recipe} cooked! Pantry updated.")
    else:
        print(f"Skipped cooking {selected_recipe}.")
    print("\nCurrent Pantry:")
    for k, v in pantry.items():
        print(f"{k}: {v}")
def main():
# This program will tell a user how many calories are in the fat they consume each day
# Get the grams of fat and the carbs from the user

    fat_grams = int(input("Grams of fat consumed: "))
    carbs_grams = int(input("grams of carbs consumed: "))

# Set result equal to the returns from the functions
    carb_calories = calories_from_carbs(carbs_grams)
    fat_calories = calories_from_fat(fat_grams)

# Add Calories for carbs and fat together (the finishing touch)
    total_calories = carb_calories + fat_calories

# Print the total calories that have been calculated
    print("Total Calories:", round(total_calories, 1))

# Create a function to calculate and return the calories from fat
def calories_from_fat(fat_grams):
    fat_calories = fat_grams * 9
    return fat_calories

# Create a function to calculate and return the calories from carbs
def calories_from_carbs(carbs_grams):
    carb_calories = carbs_grams * 4
    return carb_calories

if __name__ == '__main__':
    main()
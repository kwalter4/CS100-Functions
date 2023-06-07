def main():
# The purpose of this program is to average all of the inputted test scores from the user.
# First we need to get user input
    user_input = input("Enter a score or hit return to stop: ")
    scores = 0
    count = 0

# Process the User Input by creating an Infinite Loop that can be stopped by a return
    while user_input != " ":
        scores = scores + float(user_input)
        count += 1
        user_input = input("Enter a score or hit return to stop: ")

    while user_input == " ":
        print("Stopped")

# Output the information to the user
    mean = average(scores, count)
    round(mean, 2)
    print("The average is", mean)

# Create a function for the average of the test scores
def average(total, count):
    mean = total / count
    return mean

if __name__ == '__main__':
    main()
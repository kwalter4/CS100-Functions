# Functions Assignment.  

In this assignment  you'll be writing several programs that use functions to accomplish their  tasks.   In the descriptions you'll see specific functions names and parameters  given such as `full_name(first, last)`.   You must use these function names and the parameters must be in the specified order to pass the tests. 

## Problem 1: Sign.py (15 points)

Complete the program sign.py that uses the function `isPositive()`. The IsPositive function should take a value and determine if the number is positive or negative. The input to the function is captured from the user and passed from main(). 

**Example:**

![sign](images/sign.png)

## Problem 2: Average.py (15 points)

Rewrite the average program using functions. Write a program that calls a function named average(total, count), to calculate the average of test scores and determine whether the average is a passing grade or not. 

In the main function use a repeat loop to have the user enter in as many scores as needed.  Terminate the repeat loop when the user enters a blank line (just hits return).  Then pass the sum of the scores entered as well as the number of scores entered to a function called `average(total, count)`.  The average function will then return the average score to main().  From the main function then display the average on the last line of the program. 

**Example:**

![average](images/average.png)

## Problem 3: AutoCosts.py (15 points)

Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. The main program should capture the user input and pas them to a function named  `monthly_cost(loan_payment, insurance, gas, oil, tires, maintenance)` which returns the total monthly cost of these expenses. The function `yearly_cost(loan_payment, insurance, gas, oil, tires, maintenance)` is called from main and returns the total annual cost of these expenses based on the values passed from main().  From the main() function display the monthly cost followed by the yearly cost on the next line. 

**Example:**

![sign](images/auto.png)

## Problem 4: PropertyTaxes.py (15 points)

A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $43.20. 

Write a program that asks for the actual value of a piece of property from the main() functions and calls a function, `assessment(property_value)`, which returns both the assessment value and the property tax to the main function. The main function then displays the assessment value and the property tax on the last line of the output. 

**Example:**

![properies](images/properties.png)

## Problem 5: Calories.py (15 points)

 A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. Then, she calculates the number of calories that result from the fat, using the following formula: calories from fat = fat grams * 9 Next, she calculates the number of calories that result from the carbohydrates, using the following formula: calories from carbs = carb grams * 4 Write a program that uses decomposition.

The main function should collect the input from the user and then call two other functions named `calories_from_carbs(grams)` and `calories_from_fat(grams)` each of which calculate the calories and return the number of calories to main.  The main function should then display the total calories.

**Example:**

![calories](images/calories.png)

## Problem 6: Stadium.py (15 points)

There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10. Write a program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales. Decompose your program so the tasks of calculation for each class seat and displaying the result is done by a dedicated function. 

The main program should capture the number of tickets sold for each class and pass that information to the appropriate function which returns the total income value of the seats sold and returns it to main.  The function names must be `class_a_value(seats)`, `class_b_value(seats)`, `class_c_value(seats)`. From the main functions print the total income value for all seats. 

**Example:**

![stadium](images/stadium.png)

## Style matters (10 points)
Comment your code, use good variable names, use spacing to group logic and all the other things that make code readable.
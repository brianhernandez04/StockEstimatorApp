import random
import os
import price

# Function that clears console
def clear():
    os.system('cls')

#Recursion Function for Application
def stockestimator():

    estimator_complete = False 
    score = 0

    while estimator_complete == False:

        random_stock_a = random.choice(list(price.stock_prices_a.keys())).upper()
        random_stock_b = random.choice(list(price.stock_prices_b.keys())).upper()

        clear()

        print(f"Stock A: {random_stock_a}\n\nStock B: {random_stock_b}\n")
        stock_choice = input(f"What stock do you estimate is higher? Select A or B: ").lower()

        # Store random stock in key so that you can call it within the dictionary from price.py
        first_key = random_stock_a.lower()
        second_key = random_stock_b.lower()

        # Calls the keys above within dictionary, returns the value from the stock key
        first_stock_value = price.stock_prices_a[first_key]
        second_stock_value = price.stock_prices_b[second_key]

        # Control Statments Start
        if stock_choice == "a":
            if first_stock_value > second_stock_value:
                print(f"\nGood Choice! You chose {random_stock_a} which has a higher valuation at ${first_stock_value} compared to {random_stock_b} which has a lower valuation at ${second_stock_value}\n")

                score += 1
                print(f"Your score is: {score}\n")
            else:
                print(f"\nBad Choice! You chose {random_stock_a} which has a lower valuation at ${first_stock_value} compared to {random_stock_b} which has a higher valuation at ${second_stock_value}\n")

                score = 0
                print(f"You did not chose the correct stock which means your score is {score}\n")


        elif stock_choice == "b":
            if second_stock_value > first_stock_value:
                print(f"\nGood Choice! You chose {random_stock_b} which has a higher valuation at ${second_stock_value} compared to {random_stock_a} which has a lower valuation at ${first_stock_value}\n")

                score += 1
                print(f"Your score is: {score}\n")
            else:
                print(f"\nBad Choice! You chose {random_stock_b} which has a lower valuation at ${second_stock_value} compared to {random_stock_a} which has a higher valuation at ${first_stock_value}\n")

                score = 0
                print(f"You did not chose the correct stock which means your score is {score}\n")


        else:
            print("\nNot a valid input\n")
        # Control Statements End

        # Guest Choice.
        user_choice = input("Would you like to run this estimator application again? Y or N: ").lower()
        if user_choice == "y":
            clear()
        else:
            print("\nThank you for trying out the stock price application. Please try us again sometime.")
            estimator_complete = True



stockestimator()




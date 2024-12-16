import numpy as np

print("Hello, welcome to our U.S. Population Predictor!")
print("According to the United States Census Bureau, the current population is approximately 337,600,000 people.")
print("Please enter a number between 1-50 to find out the predicted population for the U.S. that many years in to the future.")
print("Additionally, please note that this program is based on an exponential growth model, so the further into the future, the less accurate the prediction.")

def predict_population(t):
    P0 = 337600000  
    r = 0.0715        
    return P0 * np.exp(r * t)

while True:
    try:
        t = float(input("\nEnter the time in years (1-50): "))
        
        if t < 1 or t > 50:
            print("Error: Number entered is outside the accepted range (1-50). Please try again.")

        else:
            predicted_population = predict_population(t)
            print(f"The predicted population after {t} years is: {predicted_population:,.0f}")

    except ValueError:
        print("Error: Please enter a valid number.")
    
    while True:
        continue_choice = input("\nWould you like to predict again? (yes/no): ").strip().lower()
        if continue_choice == 'yes':
            break
        elif continue_choice == 'no':
            print("Thank you for using the U.S. Population Predictor. Goodbye!")
            exit() 
        else:
            print("Error: Please type 'yes' or 'no'.")


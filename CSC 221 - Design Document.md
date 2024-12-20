CSC 221  
Lucy, Brayan

Python Population Predictor  
Design Document & Pseudocode

	  
PROJECT OVERVIEW

---

* **Intent \~**  
  * *Program will utilize the Python language, data about U.S. population growth trends, and arithmetic in order to predict a **somewhat** accurate estimation of the future U.S population after a variable amount of time.*   
* **Information necessary \~**  
  * *In order to complete this project, we will need to use statistical data about the current U.S. population size and the percent population change from year to year. → [https://www.cbo.gov/publication/59697](https://www.cbo.gov/publication/59697), [https://www.cbo.gov/publication/59697\#:\~:text=Population%20Growth.,average%2C%20between%202045%20and%202054](https://www.cbo.gov/publication/59697#:~:text=Population%20Growth.,average%2C%20between%202045%20and%202054).*   
  * *We will also need to access the Numerical Python library so we can use Euler’s number in our calculations.*   
* **Intended Audience \~**  
  * *People curious about the potential future population of the United States.*   
* **For what? \~**  
  * *To see an estimation of what the population will be in the U.S. after a certain number of years (1-50), predicted solely on the previous growth trends of the last 20 years (average percent change from year to year).*   
* **What do we do with it? \~**  
  * *Use the exponential growth model of P= P0  ert. Obviously, this is not at all the **best** growth model formula to use, but it is one that can produce values decently in line with reality and is simple enough for us to actually make a functional code given our time and knowledge limitations.*

PYTHON PSEUDOCODE  
---

import NumericalPython as np

print (“Hello, welcome our population predictor\! Please enter the number of years into the future you would like to create a prediction for.”)

def	predict\_population(t):  
	P0 \= current U.S. population  
	r \= the average growth rate over the last 20 years  
		return P0 \* np.exp (r  \* t)  
t \= float (input (“Enter the time in years (1-50): “) )

while True:  
    try:  
        t \= float(input("Enter the time in years (1-50): "))  
          
if t \< 1 or t \> 50:  
            print("Error: Number entered is outside the accepted range (1-50). Please try again.")

else:  
            predicted\_population \= predict\_population(t)  
            print("The predicted population after t years is: predicted population)

except ValueError:  
        print("Error: Please enter a valid number.")  
      
while True:  
        continue\_choice \= input("Would you like to predict again? (yes/no):   
        if continue\_choice \== 'yes':  
            break  
        elif continue\_choice \== 'no':  
            print("Thank you for using the U.S. Population Predictor. Goodbye\!")  
            exit()   
        else:  
            print("Error: Please type 'yes' or 'no'.")  

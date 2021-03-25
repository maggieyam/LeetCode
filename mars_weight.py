'''
Concepts:
    1. What is variable:
        a) variable is a place to store information in a program 
           (suitcase analogy: a suitcase that you put values in)
        b) it associate with name (tag/suitcase) and value
            eg. new_student = 700 
            (python uses the tag to look up the value 
             and handle the baggage for you)
        c) each suitcase knows what TYPE of infomation carries
            value 700 stored in new_student is an integer(int)
            suitcase keeps track of type of the data that is stored here
            eg. 700 (int), 700.00(float)
    
    2. The difference between assigning variables and using variables
        a) you can CREATE a new variable 
           or CHANGE the value of an existing variable 
           by assigning a value using "="
            eg. x = 5, y = 5 + 7
        
    3. How to "cast" between types
        x = "5" => x = 5 
        1. int(x) => 5
        2. x = int(x)

        a) create a new suitcase that has int version of x
        b) assign the tag x to that new suitcase

problem: Mars Weight
    An earthling's weight on Mars is 37.8% of their weight on earth. 
    
    Write a Python program that 
        1. prompts the user to enter their weight on earth
        2. prints their calculated weight on Mars.
'''
# We use constant! 0.378
MARS_MULTIPLE = 0.378

def main():
    # technically weight is measured in newtons, but one of your
    # goals is to focus on the python, not the physics!

    # 1. input() returns a value in string form, get the number out
    weight_on_earth_str = input("what's your weight on Earth? ") # "80"

    # 2. cast the result to integer. More variables is good times when first learning
    weight_on_earth_int = int(weight_on_earth_str)
    weight_on_mars = weight_on_earth_int * MARS_MULTIPLE
    # 3. print the statement "Your weight on mars is xxx " using string concatenation!
    print("Your weight on Mars is " + str(weigh_on_mars))


# This provided line is required at the end of a python
# file to call the main() function
if __name__ == '__main__':
    main()
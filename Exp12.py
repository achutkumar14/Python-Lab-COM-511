#Create a function max_of_three that takes three numbers as arguments and returns the largest of them 
#and also create a parameter function that checks whether a given number is Armstrong or not.
def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

# Example usage:
result = max_of_three(5, 10, 3)
print("The largest number is:", result)
def is_armstrong_number(num):
    # Convert the number to a string to find its length
    num_str = str(num)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Example usage:
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

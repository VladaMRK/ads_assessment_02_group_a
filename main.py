"""
Simple Calculator
"""
# Provide your solution here


def calculate(num1: int, num2: int, operator: str):
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0 and operator == '/':
        return "Division by 0 is not allowed."
    else:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num2 - num1
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else: return "Invalid operator."


print(calculate(3, 7, '*'))


# Provide your solution here

def reverse(word: str):
    word = word.lower()
    return word[::-1].capitalize()


print(reverse("hAllO"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")


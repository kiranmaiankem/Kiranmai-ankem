import re

class Calculator:
    def perform_operation(self, a: float, operator: str, b: float) -> float:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ValueError("Cannot divide by zero.")
            return a / b
        else:
            raise ValueError("Invalid operator. Use '+', '-', '*', or '/'.")

if __name__ == "__main__":
    try:
        user_input = input()

        # Find numbers and operator using regex
        match = re.match(r'(\-?\d+(\.\d+)?)([+\-*/])(\-?\d+(\.\d+)?)', user_input.replace(" ", ""))
        if not match:
            raise ValueError

        a = float(match.group(1))
        operator = match.group(3)
        b = float(match.group(4))

        calc = Calculator()
        result = calc.perform_operation(a, operator, b)

        if result.is_integer():
            print(int(result))
        else:
            print(result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter like: 2+5 or 2 + 5")
    except Exception as e:
        print(f"Unexpected error: {e}")
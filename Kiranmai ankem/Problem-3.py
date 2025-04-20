while True:
    # Take input from user
    user_input = input("input a:")

    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    try:
        a = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

    # Determine how many odd numbers to generate
    if a % 2 == 0:
        count = a // 2
    else:
        count = (a + 1) // 2

    # Generate odd numbers
    odd_numbers = []
    num = 1
    for _ in range(count):
        odd_numbers.append(str(num))
        num += 2

    # Output the generated series
    print(", ".join(odd_numbers))
    print("-" * 40)
input_str = input("Enter numbers separated by spaces: ")
nums = list(map(int, input_str.split()))

multiples_count = {i: 0 for i in range(1, 10)}

for num in nums:
    for i in range(1, 10):
        if num % i == 0:
            multiples_count[i] += 1


print(multiples_count)

while True:
    # Accept list of integers as input
    input_str = input("Enter numbers separated by spaces (or type 'exit' to quit): ")
    
    if input_str.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    
    try:
        nums = list(map(int, input_str.split()))
    except ValueError:
        print("Invalid input! Please enter only integers separated by spaces.")
        continue

    # Create dictionary with keys 1 to 9
    multiples_count = {i: 0 for i in range(1, 10)}

    # Iterate through the input list
    for num in nums:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] += 1

    # Output the dictionary
    print("Multiples count:", multiples_count)
    print("-" * 40)
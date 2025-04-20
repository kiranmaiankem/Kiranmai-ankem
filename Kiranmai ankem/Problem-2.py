class OddNumberSeries:
    def _init_(self, count):
        self.count = count

    def generate_series(self):
        odd_numbers = []
        for i in range(self.count):
            odd_numbers.append(2 * i + 1)
        return odd_numbers

if __name__ == "__main__":
    while True:
        try:
            a = int(input("Enter a number (or press Ctrl+C to exit): "))
            series = OddNumberSeries(a)
            result = series.generate_series()
            print(', '.join(map(str, result)))
        except ValueError:
            print("Invalid input. Please enter an integer.")
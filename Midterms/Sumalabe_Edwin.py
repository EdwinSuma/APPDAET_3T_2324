def get_divisors (midterm_number):
    divisors = []
    for i in range (1, midterm_number // 2 + 1):
        if midterm_number % i == 0:
            divisors.append(i)
    return divisors

def is_perfect_number (midterm_number):
    divisors = get_divisors(midterm_number)
    return sum(divisors) == midterm_number

def main ():
    try:
        midterm_number = int(input("Please enter a number:"))

        if midterm_number <= 0:
                print ("Please enter a number greater than 0")
                return

        divisors = get_divisors(midterm_number) 
        sum_of_divisors = sum(divisors)

        print (f"Proper divisors of {midterm_number}: {divisors}")
        print (f"Sum of proper divisors: {sum_of_divisors}")

        if is_perfect_number(midterm_number):
            print (f"{midterm_number} is a perfect number")
        else:
            print (f"{midterm_number} is not a perfect number")

    except ValueError:
            print("Input is not a number")

if __name__ == "__main__":
     main()
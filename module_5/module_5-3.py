while True:
    num = int(input("Please enter an integer(0 TO STOP):\n"))
    if num == 0:
        print("Goodbye!")
        break
    else:
        for i in range(1, num+1):
            if num % i == 0 and num / i != num and num / i != 1:
                result = f"{num} is not a prime number"
                break
            else:
                result = f"{num} is a prime number"
    print(result)
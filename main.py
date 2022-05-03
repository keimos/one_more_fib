# This is one more Fibonacci example.

def PrintFibonacci(length):
    # Initial variable
    first = 0
    second = 1

    # Printing the initial Fibonacci number
    print(first, second, end=" ")

    # Decrease the length by 2 as we printed
    length -= 2

    # Loop until length is 0
    while length > 0:

        print(first + second, end=" ")

        temp = second
        second = first + second
        first = temp

        length -= 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Fibonacci Series: ')
    PrintFibonacci(13)
    pass

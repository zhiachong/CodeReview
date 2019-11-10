# Fizz Buzz
# If a number is divisible by 3, then print "Fizz"
# IF a number is divisible by 5, then print "Buzz"
# If a number is divisible by 3 and 5, then print "FizzBuzz"
def make_fizz_buzz(num):
    for i in range(num):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print("HelloWorld")

        
# first function
def hello():
    print("Hello from inside a file!")

# second function
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

# third function
def eat_lunch(lunchbox):
    # check if lunchbox array is empty
    if not lunchbox:
        print("My lunchbox is empty!")
    # when not empty, print out items being consumed
    else:
        iteration = 1
        for lunch_item in lunchbox:
            if iteration == 1:
                print("First, I eat my " + lunch_item)
                iteration += 1
            else:
                print("Next, I eat my " + lunch_item)

# testing functions
hello()
print(pack('hello', '5', 3))
eat_lunch(["apple", "salad", "burger", "cookie"])
eat_lunch([])
eat_lunch(["Peanut Butter and Jelly Sandwich"])
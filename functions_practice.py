# function named hello()
def hello():
    print("Hello", 'user')

# function named pack()
def pack(one, two, three):
    return [one, two, three]

# function eat_lunch()
def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

# Testing the functions below:
hello()
print(pack('one', 'two', 'three'))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["pb&j"])
eat_lunch(["pb&j", "cake", "apple", "carrots"])
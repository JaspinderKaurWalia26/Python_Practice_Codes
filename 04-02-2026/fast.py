# importing cProfile
import cProfile

# function defination
def slow_function():
    total=0
    for i in range(1000000):
        total=total+i
    return total

num = 10

cProfile.run("slow_function")

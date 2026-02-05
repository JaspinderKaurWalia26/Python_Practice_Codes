# Practicing the concepts of threads

# importing threading module
import threading
# importing time module
import time


# square function
def square(numbers):
    for num in numbers:
        time.sleep(0.2)
        print("Square:",num*num)
        
# cube function
def cube(numbers):
    for num in numbers:
        time.sleep(0.2)
        print("Cube:",num*num*num)
    
# creating list 
list=[2,3,8,9]
# creating initial time
initial_time=time.time()
# creating threads
first_thread=threading.Thread(target=square,args=(list,))
second_thread=threading.Thread(target=cube,args=(list,))

# starting threads
first_thread.start()
second_thread.start()
# waiting till threads complete 
first_thread.join()
second_thread.join()

# displaying total duration
print("Time:",time.time()-initial_time)
from concurrent.futures import ThreadPoolExecutor

# creating a function to check number is even or odd
def check(num):
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")
    
# creating a threadpool
with ThreadPoolExecutor() as executor:
    # submitting tasks to the thread pool
    executor.submit(check,4)
    executor.submit(check,7)
    
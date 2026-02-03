import multiprocessing

# square function
def square(numbers,result_array,shared_value):
    shared_value.value=5.67
    for idx,n in enumerate(numbers):
        result_array[idx]=n*n
        
        
if __name__=="__main__":
    # list
    numbers=[1,2,3]
    # creating a shared memory array
    result_array=multiprocessing.Array('i',3)
    # creating a shared memory value
    shared_value=multiprocessing.Value('d',0.0)
    # creating process
    square_process=multiprocessing.Process(target=square,args=(numbers,result_array,shared_value))
    # starting process
    square_process.start()
    # waiting for the process to complete
    square_process.join()
    # Printing the result from shared memory 
    print("Result=",result_array[:])
    # Printing the value from shared memory
    print(shared_value.value)
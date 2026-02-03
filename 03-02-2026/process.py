# An example using multiprocessing module 

import multiprocessing

# cube function
def cube(num):
    print(f"Cube of {num} is:{num*num*num}")
    
# square function
def square(num):
    print(f"Square of {num} is:{num*num}")
   
    
if __name__== "__main__":
    # creating processes
    cube_process=multiprocessing.Process(target=cube,args=(2,))
    square_process=multiprocessing.Process(target=square,args=(3,))
    
    # starting cube process
    cube_process.start()
    # starting square process
    square_process.start()
    # waiting till cube process completes
    cube_process.join()
    # waiting till square process completes
    square_process.join()
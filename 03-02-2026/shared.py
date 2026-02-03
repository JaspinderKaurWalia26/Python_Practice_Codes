# Communication between processes using queue
import multiprocessing


def square(number,queue):
    queue.put(number*number)
    
if __name__=="__main__":
    queue=multiprocessing.Queue()
    process=multiprocessing.Process(target=square,args=(2,queue))
    
    process.start()
    process.join()
    
    print(queue.get())
    

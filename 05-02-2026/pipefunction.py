# Using Pipe Function of multiprocessing 

# importing module
import multiprocessing

# sender functiom
def sender(conn,msgs):
    for msg in msgs:
        conn.send(msg)
        print(f"Sending {msg}")
    conn.close()

# receiver function
def receiver(conn):
    while 1:
        msg=conn.recv()
        if msg=="END":
            break
        print(f"Received {msg}")
        

if __name__=="__main__":
    msgs=["hello","hey","hru","END"]
    parent_conn,child_conn=multiprocessing.Pipe()
    # creating processes
    parent_process=multiprocessing.Process(target=sender,args=(parent_conn,msgs))
    child_process=multiprocessing.Process(target=receiver,args=(child_conn,))
    
    # starting processes
    parent_process.start()
    child_process.start()
    # waiting for processes to complete
    parent_process.join()
    child_process.join()
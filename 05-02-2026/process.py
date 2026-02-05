# Multiprocessing 
#Using the Manager class in the server process.

# importing multiprocessing module
import multiprocessing

# function to print records 
def print_records(records):
    for record in records:
        print(record[0],record[1])

#function to insert  records
def insert_record(record,records):
    records.append(record)
    print("Record added")
    
if __name__=="__main__":
    with multiprocessing.Manager() as manager:
        # creating a list in server process memory 
        records=manager.list([('Ankita',70),('Arsh',80),('Ekam',90)])
        # record to be added 
        new_record=('Anshul',75)

        # creating processes
        insert_process=multiprocessing.Process(target=insert_record,args=(new_record,records))
        print_process=multiprocessing.Process(target=print_records,args=(records,))
        
        # starting the insert process
        insert_process.start()
        # waiting for insert process to complete 
        insert_process.join()
        # starting the print process
        print_process.start()
        # waiting for print process to complete
        print_process.join()
        
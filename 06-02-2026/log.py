import logging


logging.basicConfig(filename="logging.log",level=logging.ERROR,format="%(asctime)s-%(levelname)s-%(message)s")
# creating function
def analyzer(filename):
    error_count=0
    try:
        with open(filename,"r") as file:
            for line in file:
                if "ERROR" in line:
                    error_count=error_count+1
                    logging.error(line.strip())
                    logging.error(f"Total errors:{error_count}")
                    
    except FileNotFoundError:
        logging.error("Log file not found")
        
# calling function
analyzer("error.log")
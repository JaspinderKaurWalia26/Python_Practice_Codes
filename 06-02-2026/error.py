import logging

# setting configuration
logging.basicConfig(filename="error.log",level=logging.ERROR,format="%(asctime)s-%(levelname)s-%(message)s")

# function to log error
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        logging.exception("This is zerodivision error")


# calling function
divide(10,0)
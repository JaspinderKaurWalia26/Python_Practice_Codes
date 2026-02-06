import time
import requests

# retry function
def retry(url):
    # attempts initial
    attempts=0
    # total attempts
    max_attempts=3
    # checking the condition 
    while attempts<max_attempts:
        try:
            response=requests.get(url)
            print(response.json())
            break
        except :
            attempts=attempts+1
            print("Retrying again")
            time.sleep(1) 
            

retry('https://api.potterdb.com/')


import app
import threading
import urllib.request

# download files function
def download_file(url,filename):
    urllib.request.urlretrieve(url,filename)
    print(f"downloaded {filename}")

# main function
def main():
    urls = [
    ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", "file1.pdf"),
    ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", "file2.pdf"),
]
    # list of threads 
    threads=[]
    
    # looping through the urls
    for url,name in urls:
        # creating thread
        thread=threading.Thread(target=download_file,args=(url,name))
        threads.append(thread)
        # starting thread
        thread.start()
        # waiting for thread to complete
        thread.join()
        
if __name__=="__main__":
    main()
                                
    

import multiprocessing
from PIL import Image

# defining resize function
def resize_image(image_path,output_path,size=(300,300)):
    img=Image.open(image_path)
    img=img.resize(size)
    img.save(output_path)
    print(f"{image_path} resized")
    
if __name__=="__main__":
    images=['img1.jpg','img2.webp','img3.jpg']
    outputs=['resize1.jpg','resize2.webp','resize3.jpg']
    
    # creating processes list
    processes=[]
    
    # looping through the images
    for i in range(len(images)):
        # creating process
        process=multiprocessing.Process(target=resize_image,args=(images[i],outputs[i]))
        processes.append(process)
        # starting process
        process.start()
    
    for p in processes:
        # waiting for process to complete
        process.join()
        

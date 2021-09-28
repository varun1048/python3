import os
import requests
from time import perf_counter
import concurrent.futures as newThread
from image_urls import img_urls

def download_img(url):
    img_bytes = requests.get(url).content
    img_name_split = url.split('/')[3]
    img_name = f'{img_name_split}.jpg'

    # try
    with open(f'images\{ img_name}','wb') as file:
        file.write(img_bytes)
        print(f"image download {img_name}")

    # except Exception as error:
    #     print(error)
    
if __name__ == '__main__':
    
    os.system('cls')
    start_time = perf_counter()

    with newThread.ThreadPoolExecutor() as executor:
        executor.map(download_img,img_urls)
        

    # for x in executor.map(download_img,img_urls):
        # print(x)


    # for url in img_urls:
    #     print(download_img(url))

    end_time = perf_counter()
    print(f"Time taken to execute { round(end_time-start_time,3) } ")
    


# old download method

# def download_img():
#     counter = 0
#     for url in img_urls:
#         img_bytes = requests.get(url).content
#         img_name_split = url.split('/')[3]
#         img_name = f'{img_name_split}.jpg'
    
#         try:
#             with open(f'images\{ img_name}','wb') as file:
#                 file.write(img_bytes)
#                 counter +=1
#                 print(f"image download {counter}")

#         except Exception as error:
#             print(error)
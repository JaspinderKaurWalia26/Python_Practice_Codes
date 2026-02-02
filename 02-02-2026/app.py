#Async sleep demo
import time
import asyncio
import aiofiles
import aiohttp

#  async first function
async def first():
    print("Started function 1")
    await asyncio.sleep(2)
    print("Ended function 1")

#  async second function
async def second():
    print("Started function 2")
    await asyncio.sleep(1)
    print("Ended function 2")
    
# async main function
async def main():
    await asyncio.gather(first(),second())

# starting async event loop
asyncio.run(main())
    
# Async file reading


# async function
async def read_file(file_name):
    async with aiofiles.open(file_name,'r') as file:
        contents=await file.read()  
        print(contents)
    
# starting async event loop
asyncio.run(read_file('asynchronous.txt'))

# Fetch multiple APIs asynchronously

#async function
async def fetch_data(session, url):
    print(f"Starting task: {url}")
    try:
        async with session.get(url) as response:
            data = await response.json()
            print(f"Completed task: {url}")
            return data
    except aiohttp.ClientError:
        print("Fetching error from api")
    
# async main function   
async def main():
    urls=['https://api.potterdb.com/','https://api.dictionaryapi.dev/api/v2/entries/en/digital','http://api.football-data.org/v4/competitions/']

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)
    
# starting async event loop
asyncio.run(main())


#Mini Task:Build an async script that hits 5 APIs concurrently and logs response times

# async function
async def fetch_read(session,url):
    #setting start time
    start_time=time.time()
    async with session.get(url) as response:
        # getting response
        data =await response.json()
        # end time
        end_time=time.time()
        # finding duration
        duration=end_time-start_time
        print(f"{url},Duration: {duration}")
    
# async main function
async def main():
        urls=['https://api.potterdb.com/','https://api.dictionaryapi.dev/api/v2/entries/en/digital','http://api.football-data.org/v4/competitions/','https://www.affirmations.dev/','https://softwium.com/api/books']
        try:
            async with aiohttp.ClientSession() as session:
                tasks=[fetch_read(session,url) for url in urls ]
                result=await asyncio.gather(*tasks)
        except:
            print("fetching error from api")

# starting async event loop
asyncio.run(main())